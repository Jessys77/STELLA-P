from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
app = FastAPI(title="Scheduler MVP", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def on_startup() -> None:
    await init_db()
@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "db": "connected"}
