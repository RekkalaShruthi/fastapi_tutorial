from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title: str
    body: str
    user_id: int = 1


class BlogBase(BaseModel):
    title: str
    body: str

    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


class UserBase(BaseModel):
    name: str
    email: str

    class Config():
        from_attributes = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase] = []

    class Config():
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str
    user: UserBase

    class Config():
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
