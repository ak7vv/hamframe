# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI, Response, status

api = FastAPI()

@api.get("/config/${config_op}", status_code=status.HTTP_200_OK)
async def config(response: Response, 
                 config_op: str, 
                 config_section: str | None = None):
    
    if config_op == "export":
        return {"config_op": config_op, "config_section": config_section}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return

@api.post("/config/${config_op}")
async def config(response: Response,
                 config_op: str,
                 config_section: str | None = None):
    if config_op == "import":
        return
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
