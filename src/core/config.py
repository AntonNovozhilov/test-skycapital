from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Настройки приложения."""

    TITLE: str = "API тестовое для skycapital.group."
    VERSION: str = "1.0.0"

    POSTGRES_PORT: str
    POSTGRES_SERVER: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def db_path(self) -> str:
        """Путь к базе данных."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        """Конфигурация для настроек."""

        env_file = BASE_DIR / ".env"
        extra = "forbid"


settings = Settings()
