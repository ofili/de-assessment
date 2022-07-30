from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application
    """
    env_name: str = "DE Assessment"
    
    # db_url: str = os.environ.get("DB_URL")
    db_url = "postgresql://student:student@localhost:5432/decagon_db"

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
