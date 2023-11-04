#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pathlib

import meta
import yaml
from limedev import function_cli as main

ash = 'Æ'
file_extension = 'aedb'
path_home = pathlib.Path(__file__).parent.absolute()
path_data = path_home/ 'database'

#───────────────────────────────────────────────────────────────────────
def _load_by_name(ID='0'):
    """Loads item by its name."""
    path_file = path_data / (ID + '.' + file_extension)
    with open(path_file, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)
    return item
#───────────────────────────────────────────────────────────────────────
def _execute_from_item(item, arguments=None):
    exec(item['executable'][1])
#───────────────────────────────────────────────────────────────────────
def boot(bootitem = '0'):
    """Boots the database from the file containing boot source."""
    item = _load_by_name(ID = bootitem)
    _execute_from_item(item)


def generate() -> int:
    meta.constructor.generate_boot(path_data / '0.aedb')
    meta.constructor.generate_config(path_data / '1.aedb')
    return 0

def load() -> int:
    with open(meta.path_0, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)
    return 0


def write() -> int:
    with open(meta.path_DB/'__main__.py', 'r+') as file:
        print(file.read())
    return 0
