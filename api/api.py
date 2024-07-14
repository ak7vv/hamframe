# implement REST API using FastAPI

import sys
import os
from time import sleep
from fastapi import FastAPI
import uvicorn

from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router

api = FastAPI()

async def lifespan(api: FastAPI):
    # startup
    check_env_vars()
    api.include_router(configuration_router, prefix="/config")
    api.include_router(database_router, prefix="/db")
    api.include_router(swissarmy_router, prefix="/internal")
    yield
    # shutdown
    print("shutdown.")

api.router.lifespan_context = lifespan

def check_env_vars():
    required_vars = [ "REDIS_HOST",
                      "REDIS_PORT", 
                      "WORKERS" ]
    for var in required_vars:
        if var not in os.environ:
            raise EnvironmentError(f'env variable {var} is not set. bad image.')

if __name__ == "__main__":

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    listener_ip_address = "0.0.0.0"
    listener_port = 65432
    listener_workers = 4

    # see thread https://github.com/tiangolo/fastapi/issues/1495
    uvicorn.run(app="__main__:api", host=listener_ip_address, port=listener_port, workers=listener_workers)
