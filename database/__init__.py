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

def boot(argv):
    """Boots the database from the file containing boot source.
    argv is passed to the program implicitly"""
    path_file = pathlib.Path(__file__).parent.absolute()/ "0.aedb"
    with open(path_file, 'r+') as file:
        exec(yaml.load(file, Loader=yaml.Loader)["program"][1])
