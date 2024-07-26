# Configuration operations

from fastapi import APIRouter, Body, HTTPException, Response
from typing import Union

from pydantic import ValidationError

from globals import ConfigurationCouchbase, ConfigurationN0nbh, ConfigurationSectionName
from .get import get as configuration_get
from .put import put as configuration_put
from .patch import patch as configuration_patch
from .delete import delete as configuration_delete



router = APIRouter()



# GET

@router.get('/configuration')
@router.get('/configuration/{instance}')
@router.get('/configuration/{instance}/{section}')
async def get_config(
    response: Response,
    instance: str = None,
    section: ConfigurationSectionName = None
):
    """Handler for GET operation on configuration

    Args:
        response (Response): HTTP status code pass-through
        instance (str, optional): Name of the instance. Defaults to None.
        section (SectionName, optional): Name of the configuration section. Defaults to None.

    Returns:
        dict: HTTP operation response
    """
    return configuration_get(
        response=response,
        instance_param=instance,
        section_param=section
    )



# PUT

# @router.put('/configuration')
# @router.put('/configuration/{instance}')
@router.put('/configuration/{instance}/{section}')
async def put_config(
    response: Response,
    # data: ConfigurationCouchbase | ConfigurationN0nbh,
    instance: str,
    section: ConfigurationSectionName,
    body: dict = Body (...)
):
    """Handler for configuration PUT operation

    Args:
        response (Response): HTTP status code pass-through
        instance (str, optional): Name of the instance. Defaults to None.
        section (SectionName, optional): Name of the configuration section. 
        Defaults to None.
        body (dict, optional): Submitted configuration in body, formatted as 
        JSON and converted to dict. Defaults to Body(...).

    Returns:
        dict: HTTP operation response
    """

    print(f'instance: {instance}')
    print(f'section: {section}')
    print(f'body: {body}')
    # print(f'data: {data}')

    # if section == ConfigurationSectionName.couchbase:
    #     try:
    #         validated_data = ConfigurationCouchbase(**data.model_dump())
    #     except ValidationError as e:
    #         raise HTTPException(status_code=422, detail=e.errors())
    # elif section == ConfigurationSectionName.n0nbh:
    #     try:
    #         validated_data = ConfigurationN0nbh(**data.model_dump())
    #     except ValidationError as e:
    #         raise HTTPException(status_code=422, detail=e.errors())
    # # else:
    # #     raise HTTPException(status_code=400, detail='Invalid configuration section.')

    
    return configuration_put(
        response=response,
        instance_param=instance,
        section_param=section,
        body=body
    )



# PATCH

@router.patch('/configuration')
@router.patch('/configuration/{instance}')
@router.patch('/configuration/{instance}/{section}')
async def patch_config(
    instance: str = None,
    section: ConfigurationSectionName = None,
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
    section: ConfigurationSectionName = None
):
    return configuration_delete(
        instance_param=instance,
        section_param=section
    )