from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud.user as crud

from schemas.user import PostUser, LoginUser

router = APIRouter()


@router.post("/login")
def login_user(user: LoginUser, db: Session = Depends(get_db)):
    return


@router.post("")
def register_new_user(new_user: PostUser, db: Session = Depends(get_db)):
    return crud.create_user(db, new_user)


@router.get("")
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
