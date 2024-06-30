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
    
# import or delete configuration

@api.post("/config/${config_op}", status_code=status.HTTP_200_OK)
async def config(response: Response,
                 request: Request,
                 config_op: str,
                 instance_param: str =  Query(None, alias='instance'),
                 redis_param: str = Query(None, alias='redis'),
                 config_section: str = Query(None, alias='section') ):

    if config_op == "import" and instance_param and redis_param:
        body = await request.body()

        # did we get valid JSON in body?
        try:
            body_json = json.loads(body)
        except ValueError:
            response.status_code = status.HTTP_418_IM_A_TEAPOT # you didn't use a coffee maker
            return { 'status': 'failure', 'message': 'body is not valid JSON' }

        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param,instance_param)
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return { 'status': 'failure', 'message': 'redis connection failed' }
        # we have a working redis connection

        key='config:' + instance_param + ':' + config_section
        r.json().set(key, '.', body_json)
        print(r.json().get(key))


        # response.status_code=status.HTTP_200_OK
        return { 'status': 'success' }
    elif config_op == "delete" and instance_param and redis_param and config_section:
        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param,instance_param)
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return { 'status': 'failure', 'message': 'redis connection failed' }
        # we have a working redis connection

        key='config:' + instance_param + ':' + config_section
        
        keys_deleted = r.json().delete(key)

        # response.status_code=status.HTTP_200_OK
        return { 'status': 'success', 'message': keys_deleted + ' keys deleted' }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'status': 'failure', 'message': }
