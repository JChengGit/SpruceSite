import uuid

from db import get_db
from fastapi import APIRouter, Depends, Response
from model.user import User
from Schema.user import UserIn, UserLogin
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return {"user": user.name}


@router.post("/register")
async def create_user(item: UserIn, db: Session = Depends(get_db)):
    user = User(name=item.name, uname=item.uname, password=item.password, role=item.role)
    db.add(user)
    db.commit()
    return 1


@router.post("/login")
async def login(item: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == item.name, User.password == item.password).first()
    if not user:
        return "login failed"
    response.set_cookie(key="ticket", value=str(uuid.uuid4()))
    return "login succeed"
