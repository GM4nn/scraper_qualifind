from fastapi import APIRouter
from app.routes.router import scraper_router

api_router = APIRouter()
api_router.include_router(scraper_router)
