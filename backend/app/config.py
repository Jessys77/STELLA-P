from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR = Path(__file__).resolve().parents[2]
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
    OLLAMA_URL: str = "http://localhost:11434"
settings = Settings()
