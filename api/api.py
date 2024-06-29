# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI

api = FastAPI()

@api.get("/config/${config_op}")
async def config(config_op: str, config_section: str | None = None):
    if config_op == "export":
        return {"config_op": config_op, "config_section": config_section}
    else:
        return