# Configuration operations

from fastapi import APIRouter

router = APIRouter()

@router.get('/config/')
async def get_config():
    return [{'instance': 'instance'}]

@router.get('/config/{instance}')
async def get_config_instance_section(instance):
    return [{'instance': instance}]

@router.get('/config/{instance}/{section}')
async def get_config_instance_section(instance, section):
    return [{'instance': instance}, {'section': section}]
