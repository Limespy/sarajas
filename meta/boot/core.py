from termcolor import colored

logo = """
         AWAMMMMM  MMMMMMMMMMMM  MM       MM  MMMMMMM  MMMMA
        AWMM            MM       MM       MM  MM       MM   RA
       AW MM            MM       MM       MM  MM       MM    RD
      AW  MM            MM       MM       MM  MM       MM   RW
     AW   MMMMMMM       MM       MMMMMMMMMMM  MMMMMMM  MMWMW
    AW    MM            MM       MM       MM  MM       MM WA
   AWMMMMMMM            MM       MM       MM  MM       MM  WA
  AW      MM            MM       MM       MM  MM       MM   WA
 AW       MMMMMMM       MM       MM       MM  MMMMMMM  MM    WA"""
intro = """
Hello there!

The database has been booted, but it is not really working.

Here, have an interactive python loop instead!
"""
print(colored(logo,"white"))
print(colored(intro))

def _interactive():
    prompt = ash + ": " # Stupid hack to get the character
    while True:
        print(prompt, end="")
        exec('\n'.join(iter(input, "")))

try: 
    _interactive()
except KeyboardInterrupt:
    pass
