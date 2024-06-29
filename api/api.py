# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI, Response, status

api = FastAPI()

# export configuration

@api.get("/config/${config_op}", status_code=status.HTTP_200_OK)
async def config(response: Response, 
                 config_op: str,
                 instance: str,
                 redis: str, 
                 config_section: str | None = None ):
    
    if config_op == "export" and instance and redis:
        return {"config_op": config_op, "config_section": config_section}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
    
# import configuration

@api.post("/config/${config_op}", status_code=status.HTTP_200_OK)
async def config(response: Response,
                 config_op: str,
                 instance: str,
                 redis: str,
                 config_section: str | None = None ):

    if config_op == "import" and instance and redis:
        return
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
