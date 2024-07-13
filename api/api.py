# implement REST API using FastAPI

from os import environ
from time import sleep
from fastapi import FastAPI
import uvicorn
from .routers.configuration.operations import router as configuration_router
from .routers.database.operations import router as database_router
from .routers.internal.operations import router as swissarmy_router

api = FastAPI()

api.include_router(configuration_router, prefix="/config")
api.include_router(database_router, prefix="/db")
api.include_router(swissarmy_router, prefix="/internal")

if __name__ == "__main__":

    print(f'Hamframe API initializing.')

    redis_host = environ['REDIS_HOST']
    redis_port = environ['REDIS_PORT']

    if not redis_host:
        print(f'REDIS_HOST default not found. Bad container image.')
        fail = True
    if not redis_port:
        print(f'REDIS_PORT default not found. Bad container image.')
        fail = True

    if fail:
        print(f'Sleeping 5 seconds and exiting.')
        sleep(5) # slow down restart thrashing
        exit(1)

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    listener_ip_address = "0.0.0.0"
    listener_port = 65432
    listener_workers = 4

    print(f'API endpoint listening {listener_ip_address}:{listener_port} with {listener_workers} workers.')
    uvicorn.run("api:app", host=listener_ip_address, port=listener_port, workers=listener_workers)
