from app_init import init_data
from applog import logger
from db import get_db
from fastapi import Depends, FastAPI
from model.user import User
from router import user
from router.user import require_user
from sqlalchemy.orm import Session

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_data()


@app.get("/")
async def root():
    logger.info("request hello world test.")
    return {"message": "Hello World"}


@app.get("/db_status")
async def db_status(db: Session = Depends(get_db)):
    try:
        db.query(1)
        logger.info("test db connect OK.")
        return {"result": "OK"}
    except Exception as e:
        logger.error(f"test db connect error: {str(e)}")
        return {"result": str(e)}


@app.get("/error")
async def error():
    try:
        1/0
    except Exception as e:
        logger.error(f"What?! {str(e)}")


@app.get("/require")
async def require(user: User = Depends(require_user)):
    logger.warning(f"test require user: {user.name}")
    return user.name


app.router.include_router(user.router, prefix="/user")
