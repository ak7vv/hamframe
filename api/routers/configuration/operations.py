# Configuration operations

from enum import Enum
from fastapi import APIRouter, Body, Response

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
    response: Response,
    instance: str = None,
    section: SectionName = None
):
    """Handler for GET operation on configuration

    Args:
        response (Response): HTTP status code pass-through
        instance (str, optional): Name of the instance. Defaults to None.
        section (SectionName, optional): Name of the configuration section. Defaults to None.

    Returns:
        Dict: HTTP operation response
    """
    return configuration_get(
        response=response,
        instance_param=instance,
        section_param=section
    )



# PUT

@router.put('/configuration')
@router.put('/configuration/{instance}')
@router.put('/configuration/{instance}/{section}')
async def put_config(
    response: Response,
    instance: str = None,
    section: SectionName = None,
    body: dict = Body (...)
):
    
    return configuration_put(
        response=response,
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