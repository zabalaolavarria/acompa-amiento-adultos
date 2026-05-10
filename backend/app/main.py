from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

app = FastAPI(
    title="Acompañamiento Adultos Mayores API",
    description="API para acompañar y apoyar a adultos mayores",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de Acompañamiento Adultos Mayores",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "API funcionando correctamente"
    }

# TODO: Agregar routers
# from app.routers import auth, checkin, medicinas, mensajes, alertas, turnos
