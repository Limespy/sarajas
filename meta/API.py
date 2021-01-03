#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pathlib

from . import boot
from . import contructor
from . import texttools

path_meta = pathlib.Path(__file__).parent.absolute()
path_home = path_meta.parent
path_DB = path_home / "database"
path_0 = path_DB / "0.aedb"

