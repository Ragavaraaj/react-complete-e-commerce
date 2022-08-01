from uuid import uuid1
from sqlalchemy.orm import Session
from schemas.product import PostProduct
from models import Product


def get_product(db: Session, p_id: int):
    return db.query(Product).filter(Product.id == p_id).first()


def get_top(db: Session):
    return db.query(Product).filter(Product.rating > 3).limit(4).all()


def get_products(db: Session, keyword: str, skip: int = 0, limit: int = 100):
    if(keyword.__len__):
        search = "%{}%".format(keyword)
        return db.query(Product).filter(Product.name.like(search)).offset(skip).limit(limit).all()
    else:
        return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: PostProduct):
    gId = str(uuid1())
    db_user = Product(id=gId,
                      name=product.name,
                      brand=product.brand,
                      category=product.category,
                      description=product.description,
                      image=product.image,
                      price=product.price,
                      countInStock=product.countInStock,
                      rating=product.rating,
                      numReviews=product.numReviews)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_product(db: Session, p_id: int):
    data = db.query(Product).filter(Product.id == p_id).delete()
    db.commit()
    return data
