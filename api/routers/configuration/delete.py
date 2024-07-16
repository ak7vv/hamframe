## Delete Configuration operation

import json
from api.tooling.logger import logger
from fastapi import Request, Response, status, Query
from api.routers.database.redis import check_conf_server


async def delete_config(
        request: Request,
        response: Response,
        config_op: str,
        instance_param: str =  Query(None, alias='instance'),
        redis_param: str = Query(None, alias='redis'),
        config_section: str = Query(None, alias='section')
):

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
