"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "RenewalShield"
    APP_ENV: str = "development"
    DEBUG: bool = True
    SECRET_KEY: str = "change-me"
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    SUPABASE_SERVICE_ROLE_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
