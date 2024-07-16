# implement REST API using FastAPI

import sys
import logging
from fastapi import FastAPI
import uvicorn

from tooling import check_env_vars, set_log_level
from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router
from routers.test.operations import router as test_router



# Define API app as 'api'

api = FastAPI()



if __name__ == '__main__':

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    # see https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes for comment on worker counts

    logger = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler(sys.stdout)
    log_formatter = logging.Formatter('%(levelname)s:\t%(message)s')
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)

    # check env and use defaults if not present

    env = check_env_vars()

    # set logger level based on what we got back

    set_log_level(logger, env['LOG_LEVEL'])

    # dump environment we care about

    for var in env:
        logger.info(f'{var}={env[var]}')

    # add REST routes

    api.include_router(configuration_router, prefix='/config')
    logger.debug('/config route defined.')
    api.include_router(database_router, prefix='/db')
    logger.debug('/db route defined.')
    api.include_router(swissarmy_router, prefix='/internal')
    logger.debug('/internal route defined.')
    api.include_router(test_router, prefix='/test')
    logger.debug('/test route defined.')

    # start API

    uvicorn.run(
        app='__main__:api', 
        host=str(env['LISTENER_HOST']),
        port=int(env['LISTENER_PORT']),
        workers=int(env['LISTENER_WORKERS']),
        log_level=str(env['LOG_LEVEL'])
    )

