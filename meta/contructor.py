#!/usr/bin/python3
# -*- coding: utf-8 -*-
import yaml
from . import texttools
from . import boot
#───────────────────────────────────────────────────────────────────────
def dump_boot(path):
    key = "main_program"
    value_type = "python"
    value = boot.core_as_string
    item = {key: (value_type, value)}
    with open(path, 'w+') as file:
        yaml.dump(item, file, default_flow_style=False)
#───────────────────────────────────────────────────────────────────────