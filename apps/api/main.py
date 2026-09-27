from fastapi import FastAPI 
from app.core.config import settings 

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

@app.get("/")
def root():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }
    
@app.get("/health")
def health_check():
    return {
        "status":"healthy"
    }