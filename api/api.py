# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI

api = FastAPI()

@api.get("/")
async def read_root():
    return {"Hello": "World"}
