from typing import List, Union

from pydantic import BaseModel
from .review import Review


class ProductBase(BaseModel):
    name: str
    brand: str
    category: str
    description: str
    image: Union[str, None]
    price: float
    rating: Union[float, None]
    countInStock: int
    numReviews: int


class PostProduct(ProductBase):
    pass


class GetProduct(ProductBase):
    id: str
    reviews: Union[List[Review], None]

    class Config:
        orm_mode = True


class GetProducts(BaseModel):
    page: int = 1
    pages: int = 1
    products: List[GetProduct] = []
