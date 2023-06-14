from pydantic import BaseModel


class Url(BaseModel):
    url: str
    page: int = 1
