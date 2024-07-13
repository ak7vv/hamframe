# implement REST API using FastAPI

from fastapi import FastAPI

api = FastAPI()

api.include_router(configuration_router, prefix="/config")
api.include_router(database_router, prefix="/db")
