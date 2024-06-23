
# This does nothing terribly useful currently, and simply a crutch for
# hacking this together.

import sys
import os
import logging
from systemd import journal

import provider
from provider.configuration import *

log = logging.getLogger(__name__)
log.addHandler(journal.JournalHandler())
log.setLevel(logging.DEBUG)

log.info("test start")

toml_dict = {}

provider.configuration.toml_import(logger=log, instance_name="foo", table_name="bar", toml_dict=toml_dict)
provider.configuration.toml_export(logger=log, instance_name="foo", table_name="bar")

log.info("test complete")
