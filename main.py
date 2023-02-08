from fastapi import FastAPI

from router import user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.router.include_router(user.router, prefix="/user")
