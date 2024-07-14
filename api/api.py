# implement REST API using FastAPI

from multiprocessing import parent_process
import psutil
import sys
import os
import logging
from time import sleep
from fastapi import FastAPI,HTTPException
from contextlib import asynccontextmanager
import uvicorn



from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router
from routers.test.operations import router as test_router


logger = logging.getLogger('uvicorn.error')



# Define lifespan, setup routes

@asynccontextmanager
async def lifespan(api: FastAPI):
    # startup
    logger.debug('lifespan startup.')
    check_env_vars()
    api.include_router(configuration_router, prefix='/config')
    logger.debug('/config route defined.')
    api.include_router(database_router, prefix='/db')
    logger.debug('/db route defined.')
    api.include_router(swissarmy_router, prefix='/internal')
    logger.debug('/internal route defined.')
    api.include_router(test_router, prefix='/test')
    logger.debug('/test route defined.')
    yield
    # shutdown
    logger.info('bye.')



# Define API app as 'api'

api = FastAPI(lifespan=lifespan)



def check_env_vars():
    required_vars = [ 'REDIS_HOST',
                      'REDIS_PORT',
                      'LISTENER_IPADDR',
                      'LISTENER_PORT',
                      'LISTENER_WORKERS' ]
    for var in required_vars:
        if var not in os.environ:
            logger.critical(f'env variable {var} is not set. bad image.')
            api_shutdown() # bail now
    logger.debug(f'env is sane.')
    # we got everything, image is sane

def api_shutdown():
    ppid = os.getppid()
    parent_process = psutil.Process(ppid)
    parent_process.kill()
    sys.os.exit(1)




if __name__ == '__main__':

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    listener_host = os.environ.get('LISTENER_HOST')
    listener_port = int(os.environ.get('LISTENER_PORT'))
    # see https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes for comment on worker counts
    listener_workers = int(os.environ.get('LISTENER_WORKERS'))

    logger.debug(f'listener: {listener_host}:${listener_port} with {listener_workers} workers.')

    # start API

    # see thread https://github.com/tiangolo/fastapi/issues/1495 for uvicorn call
    try:
        uvicorn.run(app='__main__:api', host=listener_host, port=listener_port, workers=listener_workers)
    except Exception as e:
        logger.critical(f'Exception occured while running server: {e}.')
        api_shutdown()
