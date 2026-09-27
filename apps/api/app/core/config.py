from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    # Application 
    APP_NAME:str = "BisaMi AI"
    APP_VERSION:str = "0.1.0"
    DEBUG: bool = False 
    
    #API
    API_V1_PREFIX: str = "/api/v1"
    
    # Database 
    DATABASE_URL: str 
    
    #Security 
    
    JWT_SECRET_KEY: str 
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )
    
@lru_cache
def get_settings()-> Settings:
        return Settings()
    
settings = get_settings()