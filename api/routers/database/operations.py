# Database operations

import logging
from fastapi import APIRouter

def init_router(logger: logging.Logger):

    router = APIRouter()

    return router