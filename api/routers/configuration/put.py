# Configuration PUT

from fastapi import Response, status, Body
from typing import Dict
import json

from internal.check_conf_server import check_conf_server



def put(
        response: Response,
        instance_param: str = None,
        section_param: str = None,
        body: dict = Body (...)
) -> Dict:
    """Implement PUT method for
        /v1/configuration/{instance}/{section}

    Args:
        response (Response): pass through for setting specific status
        instance_param (str, optional): Name of the instance. Defaults to None.
        section_param (str, optional): Name of the configuration section. Defaults to None.
        body (dict): configuration information to store (validated JSON)

    Returns:
        Dict: response from the operation
    
    HTTP Status Codes:
        424: Redis failure
    """

    return_dict = {'instance': instance_param, 'section': section_param}

    # do we have a working Redis connection?
    redis_status, r = check_conf_server()
    if not redis_status:
        response.status_code = status.HTTP_424_FAILED_DEPENDENCY
        return { 'message': 'redis connection failed' }
    # we have a working redis connection

    # if instance_param:
    #     if section_param:
    #         key='configuration:' + instance_param + ':' + section_param
    # else:
    #     response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    #     return { 'message': 'not implemented' }


# redis code goes here

    return return_dict
