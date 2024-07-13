import requests

def get_config_section(api_url, redis_url, instance, section):

    params = {

    }

    response = requests.get(url=api_url, params=params)

    config_section = []

    return config_section