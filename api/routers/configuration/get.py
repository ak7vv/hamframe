# Get Configuration operation

from ...tooling.logger import logger
from fastapi import Request, Response, status, Query
from ..database.redis import check_conf_server

async def get_config(
        request: Request,
        response: Response, 
        config_op: str,
        instance_param: str =  Query(None, alias='instance'),
        redis_param: str = Query(None, alias='redis'),
        config_section: str | None = None
):

    route_path = request.url.path

    logger.debug(f'route_path: ${route_path}')




    if config_op == "get" and instance_param and redis_param:
        # do we have a working Redis connection?
        redis_status, r = check_conf_server(redis_param)
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
