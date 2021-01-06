class Item():
    def __init__(self, name="0"):
        self.__dict__ = _load_by_name(name=name)
        self.__name__ = name
    def execute(self):
        exec(self.executable[1])
    
    def __str__(self):
        string  = "Name:\t %s"% (self.__name__)
        for key, value in self.__dict__.items():
            if key != "__name__":
                string += "\nKey: %s:" % (key)
                string += "\tType: %s" % (value[0])
                string += "\tValue: \n%s" % (str(value[1]))
        return string

def _regenerate_boot(path = path_data / "0.aedb"):
    meta.constructor.generate_boot(path)

def _regenerate_config(path = path_data / "1.aedb"):
    meta.constructor.generate_config(path)

_boot_item = Item(name="0")
_config_item = Item(name="1")

print(_config_item.logo[1])
print(_config_item.intro[1])

prompt = ash + ": " # Stupid hack to get the symbol

try:
    while True:
        print(prompt, end="")
        exec('\n'.join(iter(input, "")))
except KeyboardInterrupt:
    pass
