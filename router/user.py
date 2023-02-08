from fastapi import APIRouter, Depends

from Schema.user import UserIn
from db import get_db
from model.user import Session, User

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
