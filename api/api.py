# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI

api = FastAPI()

# @api.get("/")
# async def read_root():
#     return {"Hello": "World"}

@api.get("/config/${config_op}/${config_section}")
async def config(config_op: str, config_section: str):
    return {"config_op": config_op, "config_section": config_section}