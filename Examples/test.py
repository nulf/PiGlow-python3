######################################################
## Set each colour to a brightness of your choosing ##
##                                                  ##
## Example by Jason - @Boeeerb                      ##
##                                                  ##
## Ported to python 3 by nulf - @nulf               ##
######################################################

from piglow import PiGlow

piglow = PiGlow(i2c_bus=1)


def ask(prompt):
    """Python 3's input() hands back a string, so the brightness has to be
    converted before it can go out over the bus as a byte."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Enter a whole number between 0 and 255.")
            continue
        if 0 <= value <= 255:
            return value
        print("Brightness must be between 0 and 255.")


piglow.white(ask("White: "))
piglow.blue(ask("Blue: "))
piglow.green(ask("Green: "))
piglow.yellow(ask("Yellow: "))
piglow.orange(ask("Orange: "))
piglow.red(ask("Red: "))
piglow.all(ask("All: "))
