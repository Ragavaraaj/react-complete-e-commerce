from fastapi import FastAPI
from models import Base
from database import engine

from api import products, users

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(products.router, prefix="/api/products")
app.include_router(users.router, prefix="/api/users")
