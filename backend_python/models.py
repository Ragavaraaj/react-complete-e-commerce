from email.policy import default
from enum import unique
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    brand = Column(String)
    category = Column(String)
    description = Column(String)
    image = Column(String)
    price = Column(Float)
    rating = Column(Float)
    countInStock = Column(Integer)
    numReviews = Column(Integer)

    reviews = relationship("Review")


class Review(Base):
    __tablename__ = "review"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    rating = Column(String)
    comment = Column(String)

    product_id = Column(String, ForeignKey("product.id"))
    product = relationship("Product", back_populates="reviews")

    user_id = Column(String, ForeignKey("user.id"))
    user = relationship("User", back_populates="reviews", uselist=False)


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    isAdmin = Column(Boolean, default=False)

    reviews = relationship("Review", back_populates="user")
