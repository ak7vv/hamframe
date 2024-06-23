
# this is used to develop and exercise the functions in the provider.configuration module
# 

import sys
import os
import logging
from cysystemd import journal
import json
import redis

import provider
from provider.configuration import *

log = logging.getLogger("config.py")
log.addHandler(journal.JournaldLogHandler())
log.setLevel(logging.DEBUG)

log.info("test start")

toml_dict = {}

provider.configuration.toml_import(logger=log, instance_name="foo", table_name="bar", toml_dict=toml_dict)
provider.configuration.toml_export(logger=log, instance_name="foo", table_name="bar")

log.info("test complete")
