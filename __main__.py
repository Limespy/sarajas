#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import yaml
import API as AetherDB
#───────────────────────────────────────────────────────────────────────
if "generate" in sys.argv:
    AetherDB.meta.constructor.generate_boot(AetherDB.path_data / "0.aedb")
    AetherDB.meta.constructor.generate_config(AetherDB.path_data / "1.aedb")

if "load" in sys.argv:
    with open(AetherDB.meta.path_0, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)

if "boot" in sys.argv:
    AetherDB.boot()

if "print" in sys.argv:
    with open(AetherDB.meta.path_DB/"__main__.py", 'r+') as file:
        print(file.read())

if "sandbox" in sys.argv:
    import sandbox