# implement REST API using FastAPI
#
# following the pattern described in 
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

API_VERSION = 'v1'

from fastapi import FastAPI
import logging

from internal import logger_init, check_env_vars, set_log_level
from routers.configuration import router as configuration_router


# check env and use defaults if not present

env = check_env_vars()

if __name__ == '__main__':
    logger = logging.getLogger('api')
    # logger = tooling.logger_init('DEBUG')

    logger_init()

    # set logger level based on what we got back

    set_log_level(env['LOG_LEVEL'])

    # dump environment we care about

    for var in env:
        logger.debug(f'env: {var}={env[var]}')
else:
    logger = logging.getLogger('uvicorn.error')

# Define API app as 'api'

api = FastAPI()

# add REST routes

api.include_router(
    router = configuration_router,
    prefix='/' + API_VERSION,
)
logger.debug('added routers.configuration')

@api.get("/")
async def root():
    return {'message': 'You\'re a tea pot?'}

# start API

if __name__ == '__main__':
    import  uvicorn

    uvicorn.run(
        app='__main__:api', 
        host=str(env['LISTENER_HOST']),
        port=int(env['LISTENER_PORT']),
        workers=int(env['LISTENER_WORKERS']),
        log_level=str(env['LOG_LEVEL'])
    )
