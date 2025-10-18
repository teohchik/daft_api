from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Daft API"
    HOST: str = "0.0.0.0"
    PORT: int = 8005

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()