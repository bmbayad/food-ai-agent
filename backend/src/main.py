import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):   
    #before app startup
    init_db()
    yield
    #after app shutdown
    

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chat")

API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

MY_PROJECT = "my simple project"


@app.get("/")
def read_index():
    return {"Hello": "World with API_KEY: " + API_KEY+ "  " + MY_PROJECT}