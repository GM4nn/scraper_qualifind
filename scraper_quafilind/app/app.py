# fastapi
from fastapi import FastAPI

# app
from config.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
