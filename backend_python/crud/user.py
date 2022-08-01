import email
from uuid import uuid1
from sqlalchemy.orm import Session
from schemas.user import PostUser
from models import User


def get_user(db: Session, p_id: int):
    return db.query(User).filter(User.id == p_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: PostUser):
    gId = str(uuid1())
    db_user = User(id=gId,
                   name=user.name,
                   email=user.email,
                   password=user.password,
                   isAdmin=user.isAdmin
                   )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, p_id: int):
    data = db.query(User).filter(User.id == p_id).delete()
    db.commit()
    return data
