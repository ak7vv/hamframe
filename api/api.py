# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI

api = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
