from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from config import settings
# import logging
from api.routes.health import healthRouter
from api.routes.appointments import router as appointments_router
from api.routes.specialties import router as specialties_router
from api.routes.doctors import router as doctors_router
from api.routes.medic_centers import router as centers_router

# /jobs/api/v1
serviceApiPrefix = ""

app = FastAPI(
    title="Medic API Endpoint",
    descriptions="Clinic X -  validate and trigger new jobs",
    version="3.0.0",
    openapi_url=f"{serviceApiPrefix}/openapi.json",
    docs_url=f"{serviceApiPrefix}/docs",
    redoc_url=f"{serviceApiPrefix}/redoc"
)

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(healthRouter, tags=["Health"])
app.include_router(appointments_router, tags=["Appointments"], prefix=f"{serviceApiPrefix}")
app.include_router(specialties_router, tags=["Specialties"], prefix=f"{serviceApiPrefix}")
app.include_router(doctors_router, tags=["Doctors"], prefix=f"{serviceApiPrefix}")
app.include_router(centers_router, tags=["Medic Centers"], prefix=f"{serviceApiPrefix}")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
