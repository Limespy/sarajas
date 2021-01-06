#!/usr/bin/python3
# -*- coding: utf-8 -*-
import yaml
from . import texttools
from . import boot
#───────────────────────────────────────────────────────────────────────
def generate_boot(path_to):
    description_text = """
    Boot item. Contains the executable for actually booting other database utilities."""

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
    item = {"description":  ("text",            description_text),
            "logo":         ("textart",         logo),
            "executable":   ("python_source",   boot.core_as_string())}
    
    with open(path_to, 'w+') as file:
        yaml.dump(item, file, default_flow_style=False)
#───────────────────────────────────────────────────────────────────────