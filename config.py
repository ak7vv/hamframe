
# this is used to develop and exercise the functions in the provider.configuration module
# 

import sys
import os
import logging
import json
import redis

import provider
from provider.configuration import *

# set up logging provider (systemd only)

log = logging.getLogger("config.py")
# log.addHandler(journal.JournaldLogHandler())
log.basicConfig(level=logging.DEBUG)

log.info("test start")

# construct dictionary

instance_name = "instance_name"
table_name = "table_name"
toml_dict = { 'instance' : instance_name, 'table' : table_name }

provider.configuration.toml_import(logger=log, redis="", toml_dict=toml_dict)
provider.configuration.toml_export(logger=log, redis="", instance_name="foo", table_name="bar")

log.info("test complete")
