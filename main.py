from applog import logger
from fastapi import Depends, FastAPI
from model.user import User
from router import user
from router.user import require_user

app = FastAPI()


@app.get("/")
async def root():
    logger.info("request hello world test.")
    return {"message": "Hello World"}


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
