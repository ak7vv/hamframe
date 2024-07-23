# implement REST API using FastAPI
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

API_VERSION = 'v1'

from fastapi import FastAPI, Response, status
import logging

from internal import logger_init, check_env_vars, set_log_level
from routers.configuration import router as configuration_router

logger = logging.getLogger('api')

if __name__ == '__main__':
    # logger = logging.getLogger('api')
    
    # logger_init()
    logger_init('DEBUG')
else:
    # logger = logging.getLogger('uvicorn.error')
    logger_init()


# check env and use defaults if not present
env = check_env_vars()

# set logger level based on what we got back
set_log_level(env['LOG_LEVEL'])

if __name__ == '__main__':
    # dump environment we care about in main process rather than each child
    for var in env:
        logger.debug(f'env: {var}={env[var]}')

# Define API app as 'api'

api = FastAPI()

# add REST routes

api.include_router(
    router = configuration_router,
    prefix='/' + API_VERSION,
)
logger.debug('added routers.configuration')

@api.get("/", )
async def root(response: Response):
    response.status_code = status.HTTP_418_IM_A_TEAPOT
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
