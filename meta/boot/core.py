class Item():
    def __init__(self, name="0"):
        self._coredict_ = _load_by_name(name=name)
        self.__dict__ = self._coredict_
        self._name_ = name
        if "_init_executable" in self.__dict__:
            exec(self._init_executable[1])
    
    def write(self):
        with open(path_data/(self._name_ + ".aedb"), 'w+') as file:
            yaml.dump(self._coredict_, file, default_flow_style=False)
    
    def execute(self):
        exec(self.executable[1])
    
    def __str__(self):
        string  = "Name:\t %s"% (self._name_)
        for key, value in self._coredict_.items():
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



print(_config.logo[1])
print(_config.intro[1])

prompt = ash + ": " # Stupid hack to get the symbol

try:
    while True:
        print(prompt, end="")
        exec('\n'.join(iter(input, "")))
except KeyboardInterrupt:
    pass
