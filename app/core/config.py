from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # 환경
    env: str = "development"
    debug: bool = True
    log_level: str = "INFO"

    # API
    api_title: str = "AI Agent Backend API"
    api_version: str = "1.0.0"
    api_prefix: str = "/api/v1"

    # 데이터베이스
    database_url: str = "postgresql://user:password@localhost:5432/ai_agent_db"
    db_echo: bool = False

    # 보안
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # 외부 API
    openai_api_key: Optional[str] = None
    claude_api_key: Optional[str] = None

    # 서버
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
