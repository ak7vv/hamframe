# Configuration GET

# from enum import Enum
from ast import Dict
from fastapi import Request, Response

# Data models

# class SectionName(str, Enum):
#     n0nbh = 'n0nbh'
#     couchbase = 'couchbase'

def get(
        response: Response,
        request: Request,
        instance_param: str = None,
        section_param: str = None
) -> Dict:

    return_dict = {'section': section_param, 'instance': instance_param}

    # match section_param:
    #     case SectionName.couchbase:
    #         return_dict.update({'message': 'i am a futon.'})
    #     case SectionName.n0nbh:
    #         return_dict.update({'message': 'it is dark.'})

    return return_dict
