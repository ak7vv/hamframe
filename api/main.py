# implement REST API using FastAPI
#
# following the pattern described in 
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

from fastapi import FastAPI
import logging

from internal import logger_init, check_env_vars, set_log_level
from routers import config

logger = logging.getLogger('api')

# Define API app as 'api'

api = FastAPI()

# start API

if __name__ == '__main__':
    import  uvicorn

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    # logger = tooling.logger_init('DEBUG')
    logger_init()

    # check env and use defaults if not present

    env = check_env_vars()

    # set logger level based on what we got back

    set_log_level(env['LOG_LEVEL'])

    # dump environment we care about

    for var in env:
        logger.debug(f'env: {var}={env[var]}')

    # add REST routes

    api.include_router(
        config.router,
        responses={418: {"description": "I'm a teapot"}},
    )
    logger.debug('config_router added')

    uvicorn.run(
        app='__main__:api', 
        host=str(env['LISTENER_HOST']),
        port=int(env['LISTENER_PORT']),
        workers=int(env['LISTENER_WORKERS']),
        log_level=str(env['LOG_LEVEL'])
    )
