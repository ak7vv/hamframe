# Database operations

import logging
from fastapi import APIRouter

def init_router() -> APIRouter:

    logger = logging.getLogger('api')

    router = APIRouter()

    return router
