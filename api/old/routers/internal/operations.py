# Swissarmy (internal) operations

# WARNING:
# unsupported for operations outside of API itself, do not call from outside of API codebase

# from api.tooling.logger_init import logger
from fastapi import APIRouter

def init_router() -> APIRouter:

    router = APIRouter()

    return router
