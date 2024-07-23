# Configuration operations

from enum import Enum
from fastapi import APIRouter, Body

router = APIRouter()



# Data models

class SectionName(str, Enum):
    n0nbh = 'n0nbh'
    couchbase = 'couchbase'



# GET

@router.get('/configuration')
async def get_config():
    return {'message': 'that\'s everything.'}

@router.get('/configuration/{instance}')
async def get_config_instance(instance: str):
    return {'instance': instance}

@router.get('/configuration/{instance}/{section}')
async def get_config_instance_section(instance: str, section: SectionName):
    match section:
        case SectionName.couchbase:
            return {'message': 'i am a futon.'}
        case SectionName.n0nbh:
            return {'message': 'it is dark.'}



# PUT

@router.put('/configuration')
async def put_config(body: dict = Body (...)):
    return body

@router.get('/configuration/{instance}')
async def put_config_instance(instance: str, body: dict = Body (...)):
    return body

@router.get('/configuration/{instance}/{section}')
async def put_config_instance_section(instance: str, section: SectionName, body: dict = Body (...)):
    return body



# PATCH

@router.patch('/configuration')
async def patch_config():
    return {'instance': 'instance'}

@router.patch('/configuration/{instance}')
async def patch_config_instance(instance: str):
    return {'instance': 'instance'}

@router.patch('/configuration/{instance}/{section}')
async def patch_config_instance_section(instance: str, section: SectionName):
    return {'instance': 'instance'}



# DELETE

@router.delete('/configuration')
async def delete_config():
    return {'message': 'he\'s dead, jim.'}

@router.delete('/configuration/{instance}')
async def delete_config_instance(instance: str):
    return {'message': 'he\'s dead, jim.'}

@router.delete('/configuration/{instance}/{section}')
async def delete_config_instance_section(instance: str, section: SectionName):
    return {'message': 'he\'s dead, jim.'}
