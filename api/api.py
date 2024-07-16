# implement REST API using FastAPI

import sys
import logging
from fastapi import FastAPI
import uvicorn

from tooling import check_env_vars, set_log_level, logger_init
from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router
# from routers.test.operations import router as test_router



# Define API app as 'api'

api = FastAPI()



if __name__ == '__main__':

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    # see https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes for comment on worker counts

    logger = logger_init() # specify 'DEBUG' if early debugging is needed

    # check env and use defaults if not present

    env = check_env_vars(logger)

    # set logger level based on what we got back

    set_log_level(logger, env['LOG_LEVEL'])

    # dump environment we care about

    for var in env:
        logger.debug(f'env: {var}={env[var]}')

    # add REST routes

    api.include_router(configuration_router, prefix='/config')
    logger.debug('route added: /config')
    api.include_router(database_router, prefix='/db')
    logger.debug('route added: /db')
    api.include_router(swissarmy_router, prefix='/internal', include_in_schema=False) # undocumented
    logger.debug('route added: /internal (undocumented)')
    # api.include_router(test_router, prefix='/test')
    # logger.debug('/test route defined.')

    # start API

    uvicorn.run(
        app='__main__:api', 
        host=str(env['LISTENER_HOST']),
        port=int(env['LISTENER_PORT']),
        workers=int(env['LISTENER_WORKERS']),
        log_level=str(env['LOG_LEVEL'])
    )

