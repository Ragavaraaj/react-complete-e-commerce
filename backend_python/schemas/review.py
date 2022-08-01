from pydantic import BaseModel


class Review(BaseModel):
    name: str
    rating: str
    comment: str
