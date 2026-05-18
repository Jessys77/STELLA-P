# Scheduler MVP - Fase 1
Scaffold base para FastAPI + PostgreSQL + Ollama + Streamlit.
## Qué incluye
- `postgres` en Docker
- `ollama` en Docker
- `backend` con FastAPI y SQLAlchemy async
- `ui` con Streamlit
- configuración por `.env`
## Requisitos
- Docker Desktop
- Docker Compose v2
## Arranque con Docker
1. Copia el archivo de ejemplo de variables:
   ```powershell
   Copy-Item .env.example .env
   ```
2. Levanta la infraestructura:
   ```powershell
   docker compose up --build
   ```
3. Verifica el backend:
   - Health: `http://localhost:8000/health`
   - Docs: `http://localhost:8000/docs`

## Si `docker` no está disponible

Si PowerShell muestra `docker : El término 'docker' no se reconoce...`, normalmente significa que Docker Desktop no está instalado, no está iniciado o la sesión de PowerShell no ha recargado el PATH.

Mientras lo resuelves, puedes ejecutar el backend en modo local con SQLite:

```powershell
cd backend
uvicorn app.main:app --reload
```

Luego prueba:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```
## UI local
La UI está en `ui/app.py`. Para ejecutarla localmente:
```powershell
streamlit run ui/app.py
```
## Backend local
Si quieres correr el backend sin Docker:
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
## Nota
El `main.py` raíz actual es un wrapper para compatibilidad. La app real vive en `backend/app/main.py`.
