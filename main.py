from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from Schema.user import UserIn
from db import get_db
from model.user import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return {"user": user.name}


@app.post("/user/register")
async def create_user(item: UserIn):
    pass
