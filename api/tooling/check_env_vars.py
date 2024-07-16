from ast import Dict
import os
from logging import Logger


def check_env_vars(logger: Logger = None) -> Dict:
    """
    Checks if environment variables we care about are present.
    If so, accept them.
    If not, substitute a reasonable default.

    Args:
        logger (Logger, optional): provide a Logger to use (for debug messages). Defaults to None.

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
        'LOG_LEVEL': 'info'
    }

    all_env_vars = dict(os.environ)
    
    env = {}

    if logger:
        logger.debug(f'all_env_vars: {all_env_vars}')
        logger.debug(f'env: {env}')

    for var in vars:
        if var in all_env_vars:
            env[var] = all_env_vars[var]
            if logger:
                logger.debug(f'selected provided {env[var]} for {var}')
        else:
            env[var] = var_defaults[var]
            if logger:
                    logger.debug(f'selected default {env[var]} for {var}')

    if logger:
        logger.debug(f'env: {env}')

    return env
