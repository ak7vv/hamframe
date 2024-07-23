# Configuration operations

from enum import Enum
from fastapi import APIRouter
import redis

router = APIRouter()

class SectionName(str, Enum):
    n0nbh = 'n0nbh'
    couchbase = 'couchbase'

@router.get('/configuration')
async def get_configuration():
    return {'instance': 'instance'}

@router.get('/configuration/{instance}')
async def get_configuration_instance(instance: str):
    return {'instance': instance}

@router.get('/configuration/{instance}/{section}')
async def get_configuration_instance_section(instance: str, section: SectionName):
    match section:
        case SectionName.couchbase:
            return {'instance': instance}, {'message': 'I am a futon.'}
        case SectionName.n0nbh:
            return {'instance': instance}, {'message': 'It is dark.'}
