from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    email: str
    isAdmin: bool


class PostUser(BaseUser):
    password: str


class GetUser(BaseUser):
    id: str


class LoginUser(BaseModel):
    email: str
    password: str
