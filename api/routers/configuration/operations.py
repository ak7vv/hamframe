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
async def get_config(
    instance: str = None,
    section: SectionName = None
):
    return configuration_get(
        instance_param=instance,
        section_param=section
    )



# PUT

@router.put('/configuration')
@router.put('/configuration/{instance}')
@router.put('/configuration/{instance}/{section}')
async def put_config(
    instance: str = None,
    section: SectionName = None,
    body: dict = Body (...)
):
    
    return configuration_put(
        instance_param=instance,
        section_param=section
    )



# PATCH

@router.patch('/configuration')
@router.patch('/configuration/{instance}')
@router.patch('/configuration/{instance}/{section}')
async def patch_config(
    instance: str = None,
    section: SectionName = None,
    body: dict = Body (...)
):

    return configuration_patch(
        instance_param=instance,
        section_param=section
    )


# DELETE

@router.delete('/configuration')
@router.delete('/configuration/{instance}')
@router.delete('/configuration/{instance}/{section}')
async def delete_config(
    instance: str = None,
    section: SectionName = None
):
    return configuration_delete(
        instance_param=instance,
        section_param=section
    )