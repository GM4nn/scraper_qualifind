from fastapi import APIRouter

tag = "scraper"
prefix = f"/{tag}"

scraper_router = APIRouter(prefix=prefix, tags=[tag], dependencies=[])
