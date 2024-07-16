# Configuration operations

from ...tooling.logger_init import logger
from fastapi import APIRouter

from .get import get_config
from .put import put_config
from .delete import delete_config

def init_router():

    router = APIRouter()
    base_path = '/config'
    
    op = 'GET'
    router.get("/", response_model=dict)(get_config)
    logger.debug(f'added {op} {base_path}/ ')
    router.get("/get", response_model=dict)(get_config)
    logger.debug(f'added {op} {base_path}/get ')

    op = 'POST'
    router.post("/", response_model=dict)(put_config)
    logger.debug(f'added {op} {base_path}/ ')
    router.post("/put", response_model=dict)(put_config)
    logger.debug(f'added {op} {base_path}/put ')
    router.post("/delete", response_model=dict)(delete_config)
    logger.debug(f'added {op} {base_path}/delete ')

    return router
