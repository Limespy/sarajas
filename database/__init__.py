#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
-
         AWAMMMMM │ database
        AWMM      │ 
       AW MM      │ The core system
      AW  MM      │ 
     AW   MMMMMMM │ 
    AW    MM      │ 
   AWMMMMMMM      │ 
  AW      MM      │ 
 AW       MMMMMMM │ 
"""
import yaml
import pathlib
ash = "Æ"
path_file = pathlib.Path(__file__).parent.absolute()
#───────────────────────────────────────────────────────────────────────
def _load_by_name(name="0"):
    """Loads item by its name"""
    path_file = pathlib.Path(__file__).parent.absolute()/ (name + ".aedb")
    with open(path_file, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)
    return item
#───────────────────────────────────────────────────────────────────────
def _execute_from_item(item, arguments=None):
    exec(item["executable"][1])
#───────────────────────────────────────────────────────────────────────
def boot():
    """Boots the database from the file containing boot source.
    """
    item = _load_by_name()
    _execute_from_item(item)
    
