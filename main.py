import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr
import resend
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Panel de Emails API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar Resend
resend.api_key = os.getenv("RESEND_API_KEY")

class EmailRequest(BaseModel):
    to: EmailStr
    sender: str
    subject: str
    html_content: str

@app.post("/api/send-email")
async def send_email(request: EmailRequest):
    try:
        params = {
            "from": request.sender,
            "to": [request.to],
            "subject": request.subject,
            "html": request.html_content,
        }
        
        email = resend.Emails.send(params)
        return {"status": "success", "message": "Email enviado correctamente", "id": email["id"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Servir archivos estáticos del frontend
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# Montar la carpeta static para otros archivos (CSS, JS)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
