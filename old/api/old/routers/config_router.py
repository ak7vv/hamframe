# Configuration operations

from fastapi import APIRouter
import logging

#from .config_get import router as get_router
from routers.configuration.config_get import router as get_router
# from .config_put import put_router
# from .config_delete import delete_router


# access the 'global' logger

logger = logging.getLogger('api')
logger.debug('foo')

router = APIRouter()

base_path = '/config'

logger.debug(f'path: {base_path}')

router.include_router(get_router, prefix='')

# op = 'GET'
# router.get(path="/", response_model=dict)(get_config)
# logger.debug(f'added {op} {base_path}/ ')
# router.get("/get", response_model=dict)(get_config)
# logger.debug(f'added {op} {base_path}/get ')

# op = 'POST'
# router.post(path="/", response_model=dict)(put_config)

# logger.debug(f'added {op} {base_path}/ ')
# router.post("/put", response_model=dict)(put_config)
# logger.debug(f'added {op} {base_path}/put ')
# router.post("/delete", response_model=dict)(delete_config)
# logger.debug(f'added {op} {base_path}/delete ')
