#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import yaml
from . import API
#───────────────────────────────────────────────────────────────────────
if "dump" in sys.argv:
    API.contructor.dump_boot(API.path_0)

if "load" in sys.argv:
    with open(API.path_0, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)

if "launchDB" in sys.argv:
    print("derp")
    from .. import database
    

if "print" in sys.argv:
    with open(API.path_DB/"__main__.py", 'r+') as file:
        print(file.read())