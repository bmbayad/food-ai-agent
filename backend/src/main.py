import os
from fastapi import FastAPI
app = FastAPI()

API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

MY_PROJECT = os.environ.get("MY_PROJECT")


@app.get("/")
def read_index():
    return {"Hello": "World with API_KEY: " + API_KEY+ "  " + MY_PROJECT}