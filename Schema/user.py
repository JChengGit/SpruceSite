from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    password: str
    role_id: int


class UserLogin(BaseModel):
    name: str
    password: str
