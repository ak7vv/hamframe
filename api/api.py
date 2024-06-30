# ripped from https://fastapi.tiangolo.com/#example

from fastapi import FastAPI, Response, status, Request, Query
import urllib.parse
from redis import *
from configuration.redis import check_conf_server
import json

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
        try:
            body_json = json.loads(body)
        except ValueError:
            response.status_code = status.HTTP_418_IM_A_TEAPOT # you didn't use a coffee maker
            return { 'status': 'failed', 'message': 'body is not valid JSON' }

        redis_status, r = check_conf_server(redis_param,instance_param)
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return { 'status': 'failed', 'message': 'redis connection failed' }
        
        # we have a valid redis connection

        r.hset('config:' + instance_param + ':' + config_section, mapping=body_json)

        # response.status_code=status.HTTP_200_OK
        return { 'status': 'success' }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'status': 'failed', 'message': 'operation not recognized' }
