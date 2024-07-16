from ast import Dict
from os import environ
from logging import Logger

def check_env_vars(logger: Logger) -> Dict:
    """
    Checks if environment variables we care about are present.
    If so, accept them.
    If not, substitute a reasonable default.

    Args:
        logger (Logger): Provide a logging.Logger to use

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
    
    env = {}

    for var in vars:
        if var not in environ:
            logger.critical(f'{var} = \'{var_defaults[var]}\' (default)')
            # The problematic exiting of fastapi/uvicorn/gunicorn and restart behavior means
            # we will populate anything not specified in required with a sane default and leave it
            # to the user to override if they have other ideas of what's sane.  Bailing is not an option.
            env[var] = var_defaults[var]
        else:
            logger.info(f'{var} = \'{environ(var)}\'')
            env[var] = environ(var)
    return env
