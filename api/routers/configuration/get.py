# Configuration GET

from fastapi import Response, status
from typing import Dict

from internal.check_conf_server import check_conf_server



def get(
        response: Response,
        instance_param: str = None,
        section_param: str = None
) -> Dict:
    """Implement GET method for 
        /v1/configuration

        /v1/configuration/{instance}
        
        /v1/configuration/{instance}/{section}

    Args:
        response (Response): pass through for setting specific status
        instance_param (str, optional): Name of the instance. Defaults to None.
        section_param (str, optional): Name of the configuration section. Defaults to None.

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

    if instance_param:
        if section_param:
            pattern='configuration:' + instance_param + ':' + section_param
        else:
            pattern = 'configuration:' + instance_param + ':*'
    else:
        pattern='configuration:*:*'

    print(f'pattern: {pattern}')

    # do something useful with redis

    return return_dict
