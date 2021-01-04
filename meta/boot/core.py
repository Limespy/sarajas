intro = """
         AWAMMMMM  MMMMMMMMMMMM  MM       MM  MMMMMMM  MMMMRD
        AWMM            MM       MM       MM  MM       MM    RD
       AW MM            MM       MM       MM  MM       MM     RD
      AW  MM            MM       MM       MM  MM       MM    RD
     AW   MMMMMMM       MM       MMMMMMMMMMM  MMMMMMM  MMWMRD
    AW    MM            MM       MM       MM  MM       MM WA
   AWMMMMMMM            MM       MM       MM  MM       MM  WA
  AW      MM            MM       MM       MM  MM       MM   WA
 AW       MMMMMMM       MM       MM       MM  MMMMMMM  MM    WA

Hello there!

The database has been booted, but it is not really working.

Here, have an interactive python loop instead!
"""

print(intro)
prompt = ash + ": " # Stupid hack to get the character
while True:
    exec(input(prompt))

