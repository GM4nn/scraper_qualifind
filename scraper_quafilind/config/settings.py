from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Scraper QuaFilind"
    API_V1_STR: str = "/api/v1"

    MODULE_NAME: str = "scraper"


settings = Settings()
