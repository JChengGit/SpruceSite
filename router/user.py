import time
import uuid

from applog import logger
from db import get_db
from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from model.user import Session as UserSession
from model.user import User
from Schema.user import UserIn, UserLogin
from sqlalchemy.orm import Session

router = APIRouter()


async def login_required(ticket: str | None = Cookie(default=None), db: Session = Depends(get_db)):
    sess = db.query(UserSession).filter(UserSession.session_key == ticket).first()
    if not sess:
        raise HTTPException(status_code=403, detail="login required")
    return sess


async def require_user(db: Session = Depends(get_db), sess: UserSession = Depends(login_required)):
    user = db.query(User).filter(User.id == sess.user_id).first()
    return user


@router.get("/")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    logger.info("request user.")
    return {"user": user.name}


@router.post("/register")
async def create_user(item: UserIn, db: Session = Depends(get_db)):
    user = User(name=item.name, uname=item.uname, password=item.password, role_id=item.role_id)
    db.add(user)
    db.commit()
    logger.info(f"create user: {user.name}")
    return "user added"


@router.post("/login")
async def login(item: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == item.name, User.password == item.password).first()
    if not user:
        return "login failed"
    ticket = str(uuid.uuid4())
    session = UserSession(session_key=ticket, user_id=user.id, user_name=user.name, create_time=time.time())
    db.add(session)
    db.commit()
    response.set_cookie(key="ticket", value=ticket)
    logger.info(f"user login: {user.name}")
    return "login succeed"


@router.post("/logout")
async def logout(user: User = Depends(require_user), db: Session = Depends(get_db)):
    db.query(UserSession).filter(UserSession.user_id == user.id).delete()
    db.commit()
    logger.info(f"user logout: {user.name}")
    return "logout succeed"
