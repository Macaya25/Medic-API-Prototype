from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from config import settings
# import logging
from api.routes.health import healthRouter
from api.routes.jobs import router as jobs_router

# /jobs/api/v1
serviceApiPrefix = ""

app = FastAPI(
    title="iaps Jobs Endpoint",
    descriptions="iaps API Jobs -  validate and trigger new jobs",
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


app.include_router(healthRouter, tags=["health"])
app.include_router(jobs_router, tags=["jobs"], prefix=f"{serviceApiPrefix}")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
