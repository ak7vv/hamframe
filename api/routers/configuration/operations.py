# Configuration operations

import logging
from fastapi import APIRouter

from .get import get_config
from .put import put_config
from .delete import delete_config

def init_router(logger: logging.Logger):

    router = APIRouter()

    router.get("/", response_model=dict)(get_config(logger=logger))
    router.get("/get", response_model=dict)(get_config(logger=logger))
    router.post("/", response_model=dict)(put_config(logger=logger))
    router.post("/put", response_model=dict)(put_config(logger=logger))
    router.post("/delete", response_model=dict)(delete_config(logger=logger))

    return router
