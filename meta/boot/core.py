class Item():
    def __init__(self, name="0", item_dict=None, ):
        if item_dict:
            self.__dict__ = item_dict
        else:
            self.__dict__  = _load_by_name(name=name)
        if "_init_executable" in self.__dict__:
            exec(self._init_executable[1])
    def addkey(self,key="test", value="value"):
        self.__dict__.update({key: value})

    def write(self):
        with open(path_data/(self._item_name[1] + ".aedb"), 'w+') as file:
            yaml.dump(self.__dict__, file, default_flow_style=False)
    
    def execute(self,**kwargs):
        exec(self.executable[1])
    
    def __str__(self):
        string  = ""
        for key, value in self.__dict__.items():
            string += "\nKey: %s:" % (key)
            string += "\tType: %s" % (value[0])
            string += "\tValue: \n%s" % (str(value[1]))
        return string

def _regenerate_boot(path = path_data / "0.aedb"):
    meta.constructor.generate_boot(path)

def _regenerate_config(path = path_data / "1.aedb"):
    meta.constructor.generate_config(path)

def _generate_item(name, item_dict):
    with open(path_data/(name + ".aedb"), 'w+') as file:
        yaml.dump(item_dict, file, default_flow_style=False)

_boot = Item(name="0")
_config = Item(name="1")
_metaindex = Item(name=_config._index_list[1])

print(_config.logo[1])
print(_config.intro[1])

prompt = ash + ": " # Stupid hack to get the symbol

try:
    while True:
        print(prompt, end="")
        exec('\n'.join(iter(input, "")))
except KeyboardInterrupt:
    pass
