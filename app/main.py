from fastapi import FastAPI

from app.users.routers import users


app = FastAPI()
app.include_router(users)
