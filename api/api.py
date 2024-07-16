# implement REST API using FastAPI

from multiprocessing import parent_process
import logging
from fastapi import FastAPI
from uvicorn import run
import uvicorn
from tooling import check_env_vars


from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router
from routers.test.operations import router as test_router


logger = logging.getLogger('uvicorn.error')

# Define API app as 'api'

api = FastAPI()

if __name__ == '__main__':

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    # see https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes for comment on worker counts

    # check env and use defaults if not present

    env = check_env_vars(logger=logger)

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

