from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Offers(BaseModel):
    lowPrice: int
    highPrice: int


class Item(BaseModel):
    name: str
    offers: Offers


class ItemListElementItem(BaseModel):
    item: Item


class ProductResponse(BaseModel):
    itemListElement: List[ItemListElementItem]
