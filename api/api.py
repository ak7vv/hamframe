# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI, Response, status, Request, Query
import urllib.parse
from redis import *
from configuration.redis import check_conf_server

api = FastAPI()

# export configuration

@api.get("/config/${config_op}", status_code=status.HTTP_200_OK)
async def config(response: Response, 
                 config_op: str,
                 instance_param: str =  Query(None, alias='instance'),
                 redis_param: str = Query(None, alias='redis'),
                 config_section: str | None = None ):
    
    if config_op == "export" and instance_param and redis_param:
        return {"config_op": config_op, "config_section": config_section}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
    
# import configuration

@api.post("/config/${config_op}", status_code=status.HTTP_200_OK)
async def config(response: Response,
                 request: Request,
                 config_op: str,
                 instance_param: str =  Query(None, alias='instance'),
                 redis_param: str = Query(None, alias='redis'),
                 config_section: str = Query(None, alias='section') ):

    if config_op == "import" and instance_param and redis_param:
        body = await request.body()
        redis_status, r = check_conf_server(redis_param,instance_param)
        
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return
        
        # response.status_code=status.HTTP_200_OK
        return 
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
