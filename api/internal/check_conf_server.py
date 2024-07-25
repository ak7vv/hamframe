
from typing import Tuple
from xmlrpc.client import Boolean
import redis
from globals import env


def check_conf_server(
    host_param: str = None, 
    port_param: str = None) -> Tuple:
    """Check if the Redis configuration endpoint is alive. 
    If host and/or port aren't provided, pull values from REDIS_HOST and REDIS_port
    environment variables
    
    Arguments:
    host_param (Optional): the Redis endpoint (.e.g, 'redis://localhost' or '127.0.0.1')
    port_param (Optional): the Redis port
    
    Return:
    (status_code, r) tuple where status_code is boolean for the check success, 
    and r is the Redis handle if successful
    """

    if not host_param:
        host_param = env['REDIS_HOST']
    if not port_param:
        port_param = env['REDIS_PORT']

    try:
        r = redis.StrictRedis(host=host_param, port=port_param, decode_responses=True )
        if r.ping():
            return True, r
        return False, None
    
    except redis.ConnectionError:
        return False, None

