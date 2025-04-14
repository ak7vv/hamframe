
env = {}
"""This Dict is set by internal.check_env_vars and contains a subset of the environment relevant to this
application.  If a value isn't provided in the environment, check_env_vars will populate a reasonable
default.  In turn, components of this application can refer to env[] to retrieve global settings to
bootstrap. 
"""

# Data models

from pydantic import BaseModel, Field, HttpUrl, field_validator, Extra
from enum import Enum

class ConfigurationSectionName(str, Enum):
    n0nbh = 'n0nbh'
    couchbase = 'couchbase'


class ConfigurationN0nbh(BaseModel):
    endpoint: HttpUrl = "https://www.hamqsl.com/solarxml.php"
    # interval: int = Field(..., ge=3600)

    @field_validator('endpoint')
    def check_https(cls, v):
        if not v.startswith('https://'):
            raise ValueError('URL must start with https://')
        return v

    class Config:
        extra = 'forbid'


class ConfigurationCouchbase(BaseModel):
    hostname: str = '127.0.0.1'
    port: int = 12345
    username: str = 'username'
    password: str = 'password'
    bucket: str = 'bucket'

    class Config:
        extra = 'forbid'
