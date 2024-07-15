# implement REST API using FastAPI

from multiprocessing import parent_process
import psutil
import sys
import os
import signal
import logging
from time import sleep
from fastapi import FastAPI
from pytest import ExitCode
import uvicorn
import asyncio



from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router
from routers.test.operations import router as test_router


logger = logging.getLogger('uvicorn.error')

# from https://stackoverflow.com/questions/75975807/how-to-stop-a-loop-on-shutdown-in-fastapi
class RuntimeVals:
    shutdown = False
    restart = False
    shutdown_complete = False

runtime_cfg = RuntimeVals

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

async def worker(n):
    while not runtime_cfg.shutdown:
        await asyncio.sleep(0.1)
    if n == 1:
        raise RuntimeError(f'This is a demo error in worker {n}')
    else:
        print(f'Worker {n} shutdown cleanly')

async def mainloop():
    loop = asyncio.get_running_loop()
    done = []
    pending = [loop.create_task(worker(1)), loop.create_task(worker(2))]

    # Handle results in the order the task are completed
    # if exeption you can handle that as well.
    while len(pending) > 0:
        done, pending = await asyncio.wait(pending)
        for task in done:
            e = task.exception()
            if e is not None:
                # This will print the exception as stack trace
                task.print_stack()
            else:
                result = task.result()
    # This is needed to kill the Uvicorn server and communicate the
    # exit code
    if runtime_cfg.restart:
        print("RESTART")
    else:
        print("SHUTDOWN")
    runtime_cfg.shutdown_complete = True
    os.kill(os.getpid(), signal.SIGINT)


@api.get("/shutdown")
async def clean_shutdown():
    runtime_cfg.shutdown = True


@api.get("/restart")
async def clean_restart():
    runtime_cfg.restart = True
    runtime_cfg.shutdown = True

@api.on_event("startup")
async def startup_event():
    loop = asyncio.get_running_loop()
    loop.create_task(mainloop())


@api.on_event("shutdown")
async def shutdown_event():
    # This is a hook point where the event
    # loop has completely shut down
    runtime_cfg.shutdown = True
    while runtime_cfg.shutdown_complete is False:
        logger.info(f'waiting')
        await asyncio.sleep(1)

if __name__ == '__main__':

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    listener_host = os.environ.get('LISTENER_HOST')
    listener_port = int(os.environ.get('LISTENER_PORT'))
    # see https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes for comment on worker counts
    listener_workers = int(os.environ.get('LISTENER_WORKERS'))

    if os.environ.get('LOG_LEVEL'):
        log_level=os.environ.get('LOG_LEVEL')
    else:
        log_level="info"

    logger.debug(f'listener: {listener_host}:${listener_port} with {listener_workers} workers with log level {log_level}.')

    # start API

    check_env_vars()
    api.include_router(configuration_router, prefix='/config')
    logger.debug('/config route defined.')
    api.include_router(database_router, prefix='/db')
    logger.debug('/db route defined.')
    api.include_router(swissarmy_router, prefix='/internal')
    logger.debug('/internal route defined.')
    api.include_router(test_router, prefix='/test')
    logger.debug('/test route defined.')

    # see thread https://github.com/tiangolo/fastapi/issues/1495 for uvicorn app call
    uv_cfg = uvicorn.Config(
        app='__main__:api', 
        host=listener_host,
        port=listener_port,
        workers=listener_workers,
        log_level=log_level,
        timeout_graceful_shutdown=2
    )
    
    server = uvicorn.Server( config=uv_cfg )
    server.run()

