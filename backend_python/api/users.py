from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud.user as crud
from schemas.user import PostUser, LoginUser
import jwt

router = APIRouter()


def generateToken(id):
    return jwt.encode({"id": id}, "YOLO_123", algorithm="HS256")


@router.post("/login")
def login_user(user: LoginUser, db: Session = Depends(get_db)):
    data = crud.get_user(db, user.email)
    return {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "isAdmin": data.isAdmin,
        "token": generateToken(data.id),
    }


@router.post("")
def register_new_user(new_user: PostUser, db: Session = Depends(get_db)):
    data = crud.create_user(db, new_user)
    return {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "isAdmin": data.isAdmin,
        "token": generateToken(data.id),
    }


@router.get("")
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
