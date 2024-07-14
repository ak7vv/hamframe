# implement REST API using FastAPI

import sys
import os
from time import sleep
from fastapi import FastAPI
import uvicorn

from routers.configuration.operations import router as configuration_router
from routers.database.operations import router as database_router
from routers.internal.operations import router as swissarmy_router

print(f'called as: {__name__}')

if __name__ == "__main__":

    print(f'Hamframe API')
    print('- bootstrap')

    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']

    if not ( redis_host and redis_port ):
        print(f'ERROR: Redis endpoint not defined. Bad container image.')
        print(f'(Sleeping 5 seconds and exiting)')
        sleep(5) # slow down restart thrashing
        exit(1)

    # stubs follow, this should be read from redis kvs for instance, section 'hamframe'

    listener_ip_address = "0.0.0.0"
    listener_port = 65432
    listener_workers = 4

    print (f'- building FastAPI routes.')

    api = FastAPI()

    api.include_router(configuration_router, prefix="/config")
    api.include_router(database_router, prefix="/db")
    api.include_router(swissarmy_router, prefix="/internal")

    print(f'- launching API endpoint')
    print(f'listener at {listener_ip_address}:{listener_port}')
    print(f'starting {listener_workers} workers')

    uvicorn.run(api, host=listener_ip_address, port=listener_port, workers=listener_workers, reload=True, verbose=True)

    print(f'exiting.')
