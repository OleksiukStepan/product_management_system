from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class ProductBase(BaseModel):
    name: str = Field(max_length=255)
    description: Optional[str] = None
    price: float = Field(ge=0)
    quantity: int = Field(0, ge=0)
    category_id: Optional[int] = None


class Product(ProductBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None


class CategoryBase(BaseModel):
    name: str = Field(max_length=255)


class Category(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str] = None
