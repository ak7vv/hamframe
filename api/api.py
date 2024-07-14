# implement REST API using FastAPI

import sys
import os
from time import sleep
from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import logging

from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router


logger = logging.getLogger('uvicorn.error')

@asynccontextmanager
async def lifespan(api: FastAPI):
    # startup
    check_env_vars()
    api.include_router(configuration_router, prefix='/config')
    logger.debug('/config route defined')
    api.include_router(database_router, prefix='/db')
    logger.debug('/db route defined')
    api.include_router(swissarmy_router, prefix='/internal')
    logger.debug('/internal route defined')
    yield
    # shutdown
    logger.info('bye.')

def check_env_vars():
    required_vars = [ 'REDIS_HOST',
                      'REDIS_PORT',
                      'LISTENER_IPADDR',
                      'LISTENER_PORT',
                      'LISTENER_WORKERS' ]
    for var in required_vars:
        if var not in os.environ:
            logger.error('env variable {var} is not set. bad image.')
            exit(1) # bail now
    # we got everything, image is sane



api = FastAPI(lifespan=lifespan)

if __name__ == '__main__':

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    listener_host = os.environ.get('LISTENER_HOST')
    listener_port = int(os.environ.get('LISTENER_PORT'))
    # see https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes for comment on worker counts
    listener_workers = int(os.environ.get('LISTENER_WORKERS'))

    logger.debug(f'listener: {listener_host}:${listener_port} with {listener_workers} workers.')

    # see thread https://github.com/tiangolo/fastapi/issues/1495 for uvicorn call
    uvicorn.run(app='__main__:api', host=listener_host, port=listener_port, workers=listener_workers)
