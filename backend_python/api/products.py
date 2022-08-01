from typing import List, Union
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import crud.product as crud

from schemas.product import GetProduct, GetProducts, PostProduct

router = APIRouter()


@router.post("")
async def post_a_new_product(new_product: PostProduct, db: Session = Depends(get_db)):
    return crud.create_product(db, new_product)


@router.get("/top", response_model=List[GetProduct])
def get_top_products(db: Session = Depends(get_db)):
    return crud.get_top(db)


@router.get("/{product_id}", response_model=GetProduct)
def get_a_single_product(product_id: str, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)


@router.delete("/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)


@router.put("/{product_id}")
def update_product(product_id: str, db: Session = Depends(get_db)):
    return {"product_id": product_id}


@router.get("", response_model=GetProducts)
def get_all_products(keyword: Union[str, None] = None, pageNumber: Union[str, None] = None, db: Session = Depends(get_db)):
    data = crud.get_products(db, keyword)
    return {
        "page": 1,
        "pages": 1,
        "products": data
    }


@router.post("/{product_id}/reviews")
def create_a_review(product_id: str, db: Session = Depends(get_db)):
    return
