from fastapi import Response

from ..providers.scraper import scraper_provider
from app.schemas.extract_product import Url
from .router import scraper_router


@scraper_router.get("/larder")
def larder():
    return scraper_provider.extract()


@scraper_router.post("/products")
def get_products_by_url(
    data: Url,
):
    return scraper_provider.extract_products(data)
