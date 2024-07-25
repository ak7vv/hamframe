# Configuration GET

from ast import Dict

def get(
        instance_param: str = None,
        section_param: str = None
) -> Dict:

    return_dict = {'instance': instance_param, 'section': section_param}

# redis code goes here

    return return_dict
