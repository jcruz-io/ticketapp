from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_ENV: str = "development"

    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "ticketapp"
    POSTGRES_DB: str = "ticketapp"
    POSTGRES_PASSWORD_FILE: Path

    @computed_field
    @property
    def database_url(self) -> str:
        password = self.POSTGRES_PASSWORD_FILE.read_text().strip()
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{password}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()
