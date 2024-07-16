from ast import Dict
import os
from logging import Logger


def check_env_vars() -> Dict:
    """
    Checks if environment variables we care about are present.
    If so, accept them.
    If not, substitute a reasonable default.

    Returns:
        Dict: returns a dictionary of environment variables and their assigned values. NOT typesafe. Consumer is resonsible for typecasting as needed.
    """

    vars = [
        'REDIS_HOST',
        'REDIS_PORT',
        'LISTENER_HOST',
        'LISTENER_PORT',
        'LISTENER_WORKERS',
        'LOG_LEVEL' 
    ]

    var_defaults = {
        'REDIS_HOST': '127.0.0.1',
        'REDIS_PORT': 6379,
        'LISTENER_HOST': '0.0.0.0',
        'LISTENER_PORT': 65432,
        'LISTENER_WORKERS': 4,
        'LOG_LEVEL': 'debug'
    }

    all_env_vars = dict(os.environ)

    env = {}

    for var in vars:
        if var in all_env_vars:
            env[var] = all_env_vars[var]
        else:
            env[var] = var_defaults[var]

    return env
