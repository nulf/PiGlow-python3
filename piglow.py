####################################################################
## Python module to control the PiGlow by Pimoroni                ##
##                                                                ##
## Original Written by Jason - @Boeeerb  -  v0.5  17/08/13        ##
##            jase@boeeerb.co.uk                                  ##
##                                                                ##
## Python 3 port written by nulf - @nulf - v0.6 07/10/26          ##
##            u@nulf.se                                           ##
##                                                                ##
####################################################################
##
## v0.6 - Port module to python 3            - 07/10/26
## v0.5 - Add RPI VER 3 for model B+         - 26/08/14
## v0.4 - Auto detect Raspberry Pi revision  - 17/08/13
## v0.3 - Added fix from topshed             - 17/08/13
## v0.2 - Code cleanup by iiSeymour          - 15/08/13
## v0.1 - Initial release                    - 15/08/13
##

try:
    from smbus import SMBus
except ImportError:
    from smbus2 import SMBus

def _detect_i2c_bus():
    """Only the original 256MB Model B (board revision 1) wired the PiGlow's
    I2C pins to bus 0; every later board, Pi 2 included, uses bus 1."""
    try:
        import RPi.GPIO as rpi
    except ImportError:
        return 1

    revision = getattr(rpi, "RPI_INFO", {}).get("P1_REVISION")
    if revision is None:
        revision = getattr(rpi, "RPI_REVISION", None)

    return 0 if revision == 1 else 1

class PiGlow:

    def __init__(self, i2c_bus=None):
        if i2c_bus is None:
            i2c_bus = _detect_i2c_bus()

        self.bus = SMBus(i2c_bus)
        self.bus.write_i2c_block_data(0x54, 0x00, [0x01])
        self.bus.write_byte_data(0x54, 0x13, 0xFF)
        self.bus.write_byte_data(0x54, 0x14, 0xFF)
        self.bus.write_byte_data(0x54, 0x15, 0xFF)

    def white(self, value):
        self.bus.write_byte_data(0x54, 0x0A, value)
        self.bus.write_byte_data(0x54, 0x0B, value)
        self.bus.write_byte_data(0x54, 0x0D, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def blue(self, value):
        self.bus.write_byte_data(0x54, 0x05, value)
        self.bus.write_byte_data(0x54, 0x0C, value)
        self.bus.write_byte_data(0x54, 0x0F, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def green(self, value):
        self.bus.write_byte_data(0x54, 0x06, value)
        self.bus.write_byte_data(0x54, 0x04, value)
        self.bus.write_byte_data(0x54, 0x0E, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def yellow(self, value):
        self.bus.write_byte_data(0x54, 0x09, value)
        self.bus.write_byte_data(0x54, 0x03, value)
        self.bus.write_byte_data(0x54, 0x10, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def orange(self, value):
        self.bus.write_byte_data(0x54, 0x08, value)
        self.bus.write_byte_data(0x54, 0x02, value)
        self.bus.write_byte_data(0x54, 0x11, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def red(self, value):
        self.bus.write_byte_data(0x54, 0x07, value)
        self.bus.write_byte_data(0x54, 0x01, value)
        self.bus.write_byte_data(0x54, 0x12, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def all(self, value):
        v = value
        self.bus.write_i2c_block_data(
            0x54, 0x01, [v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v])
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def arm(self, arm, value):
        if arm == 1:
            self.arm1(value)
        elif arm == 2:
            self.arm2(value)
        elif arm == 3:
            self.arm3(value)
        else:
            raise ValueError("Unknown arm %r, expected only 1, 2 or 3" % (arm,))

    def arm1(self, value):
        self.bus.write_byte_data(0x54, 0x07, value)
        self.bus.write_byte_data(0x54, 0x08, value)
        self.bus.write_byte_data(0x54, 0x09, value)
        self.bus.write_byte_data(0x54, 0x06, value)
        self.bus.write_byte_data(0x54, 0x05, value)
        self.bus.write_byte_data(0x54, 0x0A, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def arm2(self, value):
        self.bus.write_byte_data(0x54, 0x0B, value)
        self.bus.write_byte_data(0x54, 0x0C, value)
        self.bus.write_byte_data(0x54, 0x0E, value)
        self.bus.write_byte_data(0x54, 0x10, value)
        self.bus.write_byte_data(0x54, 0x11, value)
        self.bus.write_byte_data(0x54, 0x12, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def arm3(self, value):
        self.bus.write_byte_data(0x54, 0x01, value)
        self.bus.write_byte_data(0x54, 0x02, value)
        self.bus.write_byte_data(0x54, 0x03, value)
        self.bus.write_byte_data(0x54, 0x04, value)
        self.bus.write_byte_data(0x54, 0x0F, value)
        self.bus.write_byte_data(0x54, 0x0D, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def colour(self, colour, value):
        if colour == 1 or colour == "white":
            self.white(value)
        elif colour == 2 or colour == "blue":
            self.blue(value)
        elif colour == 3 or colour == "green":
            self.green(value)
        elif colour == 4 or colour == "yellow":
            self.yellow(value)
        elif colour == 5 or colour == "orange":
            self.orange(value)
        elif colour == 6 or colour == "red":
            self.red(value)
        else:
            raise ValueError("Only colours 1 - 6 or colour names are allowed")

    def led(self, led, value):
        leds = [
            "0x00", "0x07", "0x08", "0x09", "0x06", "0x05", "0x0A", "0x12", "0x11",
            "0x10", "0x0E", "0x0C", "0x0B", "0x01", "0x02", "0x03", "0x04", "0x0F", "0x0D"]
        self.bus.write_byte_data(0x54, int(leds[led], 16), value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led1(self, value):
        self.bus.write_byte_data(0x54, 0x07, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led2(self, value):
        self.bus.write_byte_data(0x54, 0x08, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led3(self, value):
        self.bus.write_byte_data(0x54, 0x09, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led4(self, value):
        self.bus.write_byte_data(0x54, 0x06, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led5(self, value):
        self.bus.write_byte_data(0x54, 0x05, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led6(self, value):
        self.bus.write_byte_data(0x54, 0x0A, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led7(self, value):
        self.bus.write_byte_data(0x54, 0x12, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led8(self, value):
        self.bus.write_byte_data(0x54, 0x11, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led9(self, value):
        self.bus.write_byte_data(0x54, 0x10, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led10(self, value):
        self.bus.write_byte_data(0x54, 0x0E, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led11(self, value):
        self.bus.write_byte_data(0x54, 0x0C, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led12(self, value):
        self.bus.write_byte_data(0x54, 0x0B, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led13(self, value):
        self.bus.write_byte_data(0x54, 0x01, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led14(self, value):
        self.bus.write_byte_data(0x54, 0x02, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led15(self, value):
        self.bus.write_byte_data(0x54, 0x03, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led16(self, value):
        self.bus.write_byte_data(0x54, 0x04, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led17(self, value):
        self.bus.write_byte_data(0x54, 0x0F, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led18(self, value):
        self.bus.write_byte_data(0x54, 0x0D, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)