from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str
    database_url: str
    api_title: str = "WorkoutAPI"
    api_version: str = "1.0.0"

    class Config:
        env_file = ".env"

# Instância única de configuração
settings = Settings() # type: ignore
