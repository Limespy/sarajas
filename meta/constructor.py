#!/usr/bin/python3
# -*- coding: utf-8 -*-
import yaml
from . import boot
#───────────────────────────────────────────────────────────────────────
def generate_boot(path_to=boot):
    description_text = """
    Boot item. Contains the executable for actually booting other database utilities."""
    item = {"description":  ("text",            description_text),
            "executable":   ("python_source",   boot.core_as_string())}
    
    with open(path_to, 'w+') as file:
        yaml.dump(item, file, default_flow_style=False)
#───────────────────────────────────────────────────────────────────────
def generate_config(path_to):
    description_text = """Config item."""

    logo = """
         AWAMMMMM  MMMMMMMMMMMM  MM      MM  MMMMMMMM  MMMMMA
        AWMM            MM       MM      MM  MM        MM    RA
       AW MM            MM       MM      MM  MM        MM     RD
      AW  MM            MM       MM      MM  MM        MM    RW
     AW   MMMMMMM       MM       MMMMMMMMMM  MMMMMMMM  MMWMMW
    AW    MM            MM       MM      MM  MM        MM WA
   AWMMMMMMM            MM       MM      MM  MM        MM  WA
  AW      MM            MM       MM      MM  MM        MM   WA
 AW       MMMMMMM       MM       MM      MM  MMMMMMMM  MM    WA"""
    intro = """
Hello there!

The database has been booted, but it is not really working.

Here, have an interactive python loop instead!"""
    item = {"description":  ("text",            description_text),
            "logo":         ("textart",         logo),
            "intro":        ("text",            intro)}
    with open(path_to, 'w+') as file:
        yaml.dump(item, file, default_flow_style=False)
#───────────────────────────────────────────────────────────────────────