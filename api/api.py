# implement REST API using FastAPI

from fastapi import FastAPI
from .routers.configuration.operations import router as configuration_router
from .routers.database.operations import router as database_router
from .routers.internal.operations import router as swissarmy_router

api = FastAPI()

api.include_router(configuration_router, prefix="/config")
api.include_router(database_router, prefix="/db")
api.include_router(swissarmy_router, prefix="/internal")