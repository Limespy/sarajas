#!/usr/bin/python3
# -*- coding: utf-8 -*-

import meta

key = "main_program"
value_type = "python"
value = meta.boot.core_as_string

item = {key: (value_type, value)}

import pathlib
import sys
import yaml 

path_home = pathlib.Path(__file__).parent.absolute()

name_DB = "database"

path_DB = path_home / name_DB
path_file = path_DB / "0.aedb"

if "dump" in sys.argv:
    with open(path_file, 'w+') as file:
        yaml.dump(item, file, default_flow_style=False)

if "load" in sys.argv:
    with open(path_file, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)

if "exec" in sys.argv:
    if item["main_program"][0] == "python":
        exec(item["main_program"][1])

if "print" in sys.argv:
    with open(path_DB/"__main__.py", 'r+') as file:
        print(file.read())
