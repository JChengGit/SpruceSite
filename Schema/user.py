from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    uname: str
    password: str
    role: int
