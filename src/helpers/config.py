from pydantic_settings import BaseSettings ,SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    
    APP_NAME: str 
    APP_VERSION: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE_MB: int
    FILE_DEFAULT_CHUNK_SIZE: int

    class Config:
        env_file = r"E:\ai-sales-agent\ai-sales-agent\src\.env"  # env file path
        env_file_encoding = 'utf-8'  # encoding for env file
        
        
@lru_cache()        
def get_settings():
    return Settings()