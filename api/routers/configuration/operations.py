# Configuration operations

from enum import Enum
from fastapi import APIRouter, Body, Request, Response

from .get import get as configuration_get
from .put import put as configuration_put
from .patch import patch as configuration_patch
from .delete import delete as configuration_delete



router = APIRouter()



# Data models

class SectionName(str, Enum):
    n0nbh = 'n0nbh'
    couchbase = 'couchbase'



# GET

@router.get('/configuration')
async def get_config_all(
    request: Request,
    response: Response
):
    # get(
    #     request=request,
    #     response=response,
    # )
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
async def put_config_all(body: dict = Body (...)):
    return body

@router.get('/configuration/{instance}')
async def put_config_instance(instance: str, body: dict = Body (...)):
    return body

@router.get('/configuration/{instance}/{section}')
async def put_config_instance_section(instance: str, section: SectionName, body: dict = Body (...)):
    return body



# PATCH

@router.patch('/configuration')
async def patch_config_all():
    return {'instance': 'instance'}

@router.patch('/configuration/{instance}')
async def patch_config_instance(instance: str):
    return {'instance': 'instance'}

@router.patch('/configuration/{instance}/{section}')
async def patch_config_instance_section(instance: str, section: SectionName):
    return {'instance': 'instance'}



# DELETE

@router.delete('/configuration')
async def delete_config_all():
    return {'message': 'he\'s dead, jim.'}

@router.delete('/configuration/{instance}')
async def delete_config_instance(instance: str):
    return {'message': 'he\'s dead, jim.'}

@router.delete('/configuration/{instance}/{section}')
async def delete_config_instance_section(instance: str, section: SectionName):
    return {'message': 'he\'s dead, jim.'}
