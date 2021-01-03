import pathlib

path_boot = pathlib.Path(__file__).parent.absolute()

from .. import texttools

core_as_string = texttools.filepath2string(path_boot / "core.py")