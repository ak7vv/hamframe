# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI

api = FastAPI()

@api.get("/config/${config_op}")
async def config(config_op: str, config_section: str):
    return {"config_op": config_op, "config_section": config_section}