# implement REST API using FastAPI

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
        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param,instance_param)
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return { 'status': 'failure', 'message': 'redis connection failed' }
        # we have a working redis connection
        
        # construct pattern and retrieve value
        if config_section:
            pattern='config:' + instance_param + ':' + config_section
        else:
            pattern = 'config:' + instance_param + ':*'
        
        keys = r.keys(pattern=pattern)
        print(keys)
        if keys:
            json = {}
            for key in keys:
                print(key)
                value=r.json().get(key, '.')
                json[len(json)+1] = { 'section': key.split(':')[2], 'value': value }
            json |= { 'status': 'success', 'message': 'section(s) matching \'' + pattern + '\'', 'sections': len(keys) }
            response.status_code = status.HTTP_200_OK
            return json
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {'status': 'failure', 'message': 'key \'' + pattern + '\' does not exist' }

    else:
        response.status_code = status.HTTP_501_NOT_IMPLEMENTED
        return { 'status': 'failure', 'message': 'operation \'' + config_op + '\' not recognized' }
    
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
            response.status_code = status.HTTP_418_IM_A_TEAPOT # you didn't try to make tea
            return { 'status': 'failure', 'message': 'body is not valid JSON' }

        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param,instance_param)
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return { 'status': 'failure', 'message': 'redis connection failed' }
        # we have a working redis connection

        # construct key and set value
        key='config:' + instance_param + ':' + config_section

        r.json().set(key, '.', body_json)

        # response.status_code=status.HTTP_200_OK
        return { 'status': 'success', 'message': 'key \'' + key + '\' created' }
    

    elif config_op == "delete" and instance_param and redis_param:
        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param,instance_param)
        if not redis_status:
            response.status_code = status.HTTP_502_BAD_GATEWAY
            return { 'status': 'failure', 'message': 'redis connection failed' }
        # we have a working redis connection

        # did we get a specific section to delete?
        if config_section:
            pattern = 'config:' + instance_param + ':' + config_section
        else: # bulk delete
            pattern = 'config:' + instance_param + ':*'

        cursor = '0'
        while  cursor != 0:
            cursor, keys = r.scan(cursor=cursor, match=pattern, count=100)
            if keys:
                try:
                    r.delete(*keys)
                except:
                    response.status_code = status.HTTP_502_BAD_GATEWAY
                    return { 'status': 'failure', 'message': 'redis connection failed' }

        response.status_code = status.HTTP_202_ACCEPTED
        return { 'status': 'success', 'message': 'no keys matching \'' + pattern + '\' remaining in instance', 'sections': len(keys) }
    else:
        response.status_code = status.HTTP_501_NOT_IMPLEMENTED
        return { 'status': 'failure', 'message': 'operation \'' + config_op + '\' not recognized' }
