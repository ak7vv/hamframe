
# This does nothing terribly useful currently, and simply a crutch for
# hacking this together.

import sys
import os

import provider
from provider.configuration import *

provider.configuration.toml_import()
provider.configuration.toml_export()

