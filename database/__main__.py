#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import yaml
import pathlib
path_file = pathlib.Path(__file__).parent.absolute()/ "0.aedb"

argv = sys.argv

with open(path_file, 'r+') as outfile:
    item = yaml.load(outfile, Loader=yaml.Loader)
    if item["main_program"][0] == "python":
        exec(item["main_program"][1])
