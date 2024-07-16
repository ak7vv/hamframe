# Swissarmy (internal) operations

# WARNING:
# unsupported for operations outside of API itself, do not call from outside of API codebase

import logging
from fastapi import APIRouter

def init_router(logger: logging.Logger):

    router = APIRouter()

    return router