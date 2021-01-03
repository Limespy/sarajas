#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import yaml
import meta
#───────────────────────────────────────────────────────────────────────
if "dump" in sys.argv:
    meta.contructor.dump_boot(meta.path_0)

if "load" in sys.argv:
    with open(meta.path_0, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)

if "launchDB" in sys.argv:
    print("derp")
    import database
    database.boot(sys.argv)

if "print" in sys.argv:
    with open(meta.path_DB/"__main__.py", 'r+') as file:
        print(file.read())