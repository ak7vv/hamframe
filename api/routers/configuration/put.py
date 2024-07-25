# Configuration PUT

from ast import Dict
from fastapi import Response, status

def put(
        response: Response,
        instance_param: str = None,
        section_param: str = None        
) -> Dict:
    
    return_dict = {'instance': instance_param, 'section': section_param}

# redis code goes here

    return return_dict
