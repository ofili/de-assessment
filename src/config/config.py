from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Settings for the application
    """
    env_name: str = "APP_ENV"

    base_url: str = "http://localhost:5000"
    db_url: str = "postgresql://student:student@localhost:5432/decagon_db"
    
    class Config:
        """
        Config for the application
        """
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    """
    Get the settings for the application
    """
    settings = Settings()
    print(f'Loading settings from {settings.env_name} environment')
    return settings
