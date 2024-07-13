# Configuration operations

from fastapi import APIRouter
from .get import get_config
from .put import put_config
from .delete import delete_config

router = APIRouter()

router.get("/", response_model=dict)(get_config)
router.get("/get", response_model=dict)(get_config)
router.post("/", response_model=dict)(put_config)
router.post("/put", response_model=dict)(put_config)
router.post("/delete", response_model=dict)(delete_config)
