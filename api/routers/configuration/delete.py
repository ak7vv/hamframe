# Configuration DELETE

from ast import Dict
from fastapi import Response, status

def delete(
        response: Response,
        instance_param: str = None,
        section_param: str = None
) -> Dict:

    return_dict = {'instance': instance_param, 'section': section_param}

# redis code goes here

    return return_dict
