#!/usr/bin/python3
# -*- coding: utf-8 -*-
import yaml
from . import texttools
from . import boot
#───────────────────────────────────────────────────────────────────────
def generate_boot(path):
    key = "program"
    value_type = "python_source"
    value = boot.core_as_string
    item = {key: (value_type, value)}
    with open(path, 'w+') as file:
        yaml.dump(item, file, default_flow_style=False)
#───────────────────────────────────────────────────────────────────────