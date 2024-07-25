# Configuration operations

from enum import Enum
from typing import Optional
from fastapi import APIRouter, Body, Path, Request, Response, Query

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
@router.get('/configuration/{instance}')
@router.get('/configuration/{instance}/{section}')
def get_config(
    request: Request,
    response: Response,
    instance: str = None,
    section: SectionName = None
):
    return_dict = configuration_get(
        request=request,
        response=response,
        instance_param=instance,
        section_param=section
    )
    
    print(f'return_dict: {return_dict}')

    return return_dict




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
