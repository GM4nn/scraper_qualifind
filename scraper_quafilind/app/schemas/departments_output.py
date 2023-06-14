from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Subcategory(BaseModel):
    name: Optional[str]
    url: Optional[str]


class Category(BaseModel):
    name: Optional[str]
    url: Optional[str]
    subcategories: Optional[List[Subcategory]]


class Department(BaseModel):
    department: Optional[str]
    url: Optional[str]
    categories: Optional[List[Category]]
