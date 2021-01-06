from termcolor import colored

intro = """
Hello there!

The database has been booted, but it is not really working.

Here, have an interactive python loop instead!"""
#───────────────────────────────────────────────────────────────────────
class Item():
    def __init__(self, name="0"):
        self.__dict__ = _load_by_name(name=name)
        self.__name__ = name
    def execute(self):
        exec(self.executable[1])
    
    def __str__(self):
        string  = "Item name:\t %s" (self.__name__)
        return string
#───────────────────────────────────────────────────────────────────────
def _regenerate_boot():
    meta.constructor.generate_boot(meta.path_0)
#───────────────────────────────────────────────────────────────────────
item = Item()
print(colored(item.logo[1],"white"))
print(colored(intro))
prompt = ash + ": " # Stupid hack to get the character
#───────────────────────────────────────────────────────────────────────
try:  # The infinite interactive loop. Exit with command exit()
    while True:
        print(prompt, end="")
        exec('\n'.join(iter(input, "")))
except KeyboardInterrupt:
    pass
