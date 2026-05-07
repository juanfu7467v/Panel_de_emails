# 📧 Panel de Emails Profesional

Este es un sistema completo para gestionar y enviar correos electrónicos con plantillas HTML/CSS personalizadas utilizando la API de **Resend**.

## 🚀 Características

- **Interfaz Moderna:** Panel administrativo limpio y responsive (Tailwind CSS).
- **Editor de Plantillas:** Escribe o pega tu código HTML/CSS y mira los cambios al instante.
- **Vista Previa:** Visualiza cómo se verá el correo antes de enviarlo.
- **Backend Robusto:** Desarrollado con FastAPI y validaciones de Pydantic.
- **Listo para Producción:** Configurado para desplegarse en **Fly.io**.

## 🛠️ Tecnologías

- **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla).
- **Backend:** Python, FastAPI, Resend SDK.
- **Despliegue:** Docker, Fly.io.

## ⚙️ Configuración Local

1. Clona el repositorio.
2. Crea un archivo `.env` basado en `.env.example` y añade tu `RESEND_API_KEY`.
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta el servidor:
   ```bash
   python main.py
   ```
5. Abre `http://localhost:8080` en tu navegador.

## 🚢 Despliegue en Fly.io

1. Instala [flyctl](https://fly.io/docs/hands-on/install-flyctl/).
2. Inicia sesión: `fly auth login`.
3. Crea la app: `fly apps create panel-de-emails`.
4. Configura el secret de Resend:
   ```bash
   fly secrets set RESEND_API_KEY=tu_api_key_aqui
   ```
5. Despliega:
   ```bash
   fly deploy
   ```

---
Desarrollado con ❤️ para una gestión de emails eficiente.
