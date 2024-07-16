# Put Configuration operation

import json
# from ...tooling.logger_init import logger
from fastapi import Request, Response, status, Query
from ..database.redis import check_conf_server

async def put_config(
        request: Request,
        response: Response,
        config_op: str,
        instance_param: str =  Query(None, alias='instance'),
        redis_param: str = Query(None, alias='redis'),
        config_section: str = Query(None, alias='section')
):

    route_path = request.url.path



    if config_op == "put" and instance_param and redis_param:
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
        # we have a working redis connection

        # construct key and set value
        key='config:' + instance_param + ':' + config_section

        r.json().set(key, '.', body_json)

        # response.status_code=status.HTTP_200_OK
        return { 'status': 'success', 'message': 'key \'' + key + '\' created' }
