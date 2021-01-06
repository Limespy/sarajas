#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
import pathlib
import meta

ash = "Æ"
path_home = pathlib.Path(__file__).parent.absolute()
path_data = path_home/ "database"
#───────────────────────────────────────────────────────────────────────
def _load_by_name(name="0"):
    """Loads item by its name"""
    path_file = path_data / (name + ".aedb")
    with open(path_file, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)
    return item
#───────────────────────────────────────────────────────────────────────
def _execute_from_item(item, arguments=None):
    exec(item["executable"][1])
#───────────────────────────────────────────────────────────────────────
def boot(bootitem = "0"):
    """Boots the database from the file containing boot source.
    """
    item = _load_by_name(name = bootitem)
    _execute_from_item(item)