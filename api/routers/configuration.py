# Configuration operations

from fastapi import APIRouter

router = APIRouter()

@router.get('/configuration')
async def get_configuration():
    return {'instance': 'instance'}

@router.get('/configuration/{instance}')
async def get_configuration_instance(instance: str):
    return {'instance': instance}

@router.get('/configuration/{instance}/{section}')
async def get_configuration_instance_section(instance: str, section: str):
    return {'instance': instance}, {'section': section}
