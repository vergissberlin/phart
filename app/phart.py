from signal import pause
from gpiozero import Button
import photo
import draw
import convert
import config

from os import system
system("pigpiod")

# 1. **Photo**
# 1.1 Pulse() RED light
# 1.2 Blink flash light 3 times short
# 1.3 Take a photo with long flash light
# 1.4 Turn off flash light
# 1.5 Solid RED light
# 2. **Converting**
# 2.1 Pulse() YELLOW light
# 2.2 Convert it into paths
# 2.3 Solid YELLOW light
# 3. **Draw it**
# 3.1 Pulse() GREEN light
# 3.2 Draw it with the plotter
# 3.3 Solid GREEN light


# Read the configuration
exec(open('config.py').read())


# Project version number
__version__ = '0.0.1'


class PhArt:
    def __init__(self, ):
        print("Welcom to PhArt! pfffff")

    @staticmethod
    def say_hello():
        print("Hello!")


button = Button(PIN_BUTTON)
button.when_pressed = PhArt.say_hello()

pause()
