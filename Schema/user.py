from pydantic import BaseModel


class UserIn(BaseModel):
    id: int
    name: str
    uname: str
    password: str
    role: int
