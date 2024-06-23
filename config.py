
# This does nothing terribly useful currently, and simply a crutch for
# hacking this together.

import sys
import os
import logging
from systemd.journal import JournalHandler

import provider
from provider.configuration import *

log = logging.getLogger(__name__)
log.addHandler(JournalHandler())
log.setLevel(logging.DEBUG)

log.info("config test start")

provider.configuration.toml_import()
provider.configuration.toml_export()

log.info("config test complete")
