## Delete Configuration operation

import json
from fastapi import Request, Response, status, Query
from ..database.redis import check_conf_server


async def delete_config(request: Request,
                        response: Response,
                        config_op: str,
                        instance_param: str =  Query(None, alias='instance'),
                        redis_param: str = Query(None, alias='redis'),
                        config_section: str = Query(None, alias='section') ):

    route_path = request.url.path

    if config_op == "delete" and instance_param and redis_param:
        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param)
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


# Database operations



@api.get("/db/${db_op}", status_code=status.HTTP_200_OK)
async def get_db(response: Response, 
                 db_op: str,
                 instance_param: str =  Query(None, alias='instance'),
                 redis_param: str = Query(None, alias='redis')):

        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param)
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return { 'status': 'failure', 'message': 'redis connection failed' }
        # we have a working redis connection

        return {'status': 'success', 'message': 'noop'}



@api.post("/db/${db_op}", status_code=status.HTTP_200_OK)
async def post_db(response: Response,
                 request: Request,
                 db_op: str,
                 instance_param: str =  Query(None, alias='instance'),
                 redis_param: str = Query(None, alias='redis')):

    if db_op == "foo" and instance_param and redis_param:
        body = await request.body()

        # did we get valid JSON in body?
        try:
            body_json = json.loads(body)
        except ValueError:
            response.status_code = status.HTTP_418_IM_A_TEAPOT # you didn't try to make tea
            return { 'status': 'failure', 'message': 'body is not valid JSON' }
    
        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param)
        if not redis_status:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return { 'status': 'failure', 'message': 'redis connection failed' }


        # get Couchbase config from Redis



        # do we have a working Couchbase connection?
                
        # couchbase_status, couchbase = check_conf_server(couchbase_param)

        json = body_json
        json |= { 'status': 'success', 'message': 'submitted' }
        
        return json

    else:
        response.status_code = status.HTTP_501_NOT_IMPLEMENTED
        return { 'status': 'failure', 'message': 'operation \'' + db_op + '\' not recognized' }

