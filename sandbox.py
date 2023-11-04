#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pathlib
import pprint

import yaml
from atherdb import meta

pp = pprint.PrettyPrinter(indent=4)

ash = 'Æ'
file_extension = 'aedb'
path_home = pathlib.Path(__file__).parent.absolute()
path_data = path_home/ 'database'

#───────────────────────────────────────────────────────────────────────
def _load_by_name(ID='0'):
    """Loads item by its name."""
    path_file = path_data / (ID + '.' + file_extension)
    with open(path_file, 'r+') as file:
        item = yaml.load(file, Loader=yaml.Loader)
    return item
#───────────────────────────────────────────────────────────────────────
def _execute_from_item(item, arguments=None):
    exec(item['executable'][1])
#───────────────────────────────────────────────────────────────────────
def boot(bootitem = '0'):
    """Boots the database from the file containing boot source."""
    item = _load_by_name(ID = bootitem)
    _execute_from_item(item)
#───────────────────────────────────────────────────────────────────────
#───────────────────────────────────────────────────────────────────────
class Datum():
    def __init__(self, datum):
        self._type = datum[0]
        self.value = datum[1]
    def __str__(self):
        return str(self.value)
class Item():
    def __init__(self, ID='0', item_dict=None):
        if item_dict:
            self._unpack(item_dict)
        else:
            self._unpack(_load_by_name(ID=str(ID)))
        if '_init_executable' in self.__dict__:
            exec(self._init_executable[1]) # type: ignore

    def _unpack(self, item_dict):
        self.__dict__ = {key: Datum(datum_tuple) for key, datum_tuple in item_dict.items()}

    def add_key(self,key='test', dtype='_python_str', value='value'):
        self.__dict__.update({key: Datum((dtype, value))})

    def write(self):
        """Packs and writes the item back."""
        packed_dict = {key: (d._type, d.value) for key, d in self.__dict__.items()}
        path = path_data/(str(self.__ID__) + '.' + file_extension) # type: ignore
        with open(path, 'w+') as file:
            yaml.dump(packed_dict, file, default_flow_style=False)

    def execute(self,**kwargs):
        exec(self.executable[1]) # type: ignore

    def __str__(self):
        string  = ''
        for key, datum in self.__dict__.items():
            string += '\nKey: %s:' % (key)
            string += '\tType: %s' % (datum._type)
            string += '\tValue: \n%s' % (str(datum))
        return string

def _regen(path = path_data / '0.aedb'):
    meta.constructor.generate_boot(path_data / '0.aedb')
    meta.constructor.generate_config(path_data / '1.aedb')

_boot = Item(ID='0')
_config = Item(ID='1')
_types = Item(ID=_config._types) # type: ignore
_metaindex = Item(ID=_config._metaindex) # type: ignore

print(_config.logo) # type: ignore
print(_config.intro) # type: ignore
try:
    prompt = ash + ': ' # Stupid hack to get the symbol
    while True:
        print(prompt, end='')
        exec('\n'.join(iter(input, '')))
except KeyboardInterrupt:
    pass
