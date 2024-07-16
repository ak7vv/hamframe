# Swissarmy (internal) operations

# WARNING:
# unsupported for operations outside of API itself, do not call from outside of API codebase

from ...tooling.logger_init import logger
from fastapi import APIRouter

def init_router():

    router = APIRouter()

    return router
