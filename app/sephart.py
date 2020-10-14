from datetime import datetime
from gpiozero import Button, LED
from picamera import PiCamera
from signal import pause
from time import sleep

# Read the configuration
exec(open('config.py').read())

#from os import system
# system("pigpiod")


# 3. **Draw it**
# 3.1 Pulse() GREEN light
# 3.2 Draw it with the plotter
# 3.3 Solid GREEN light


# Read the configuration
exec(open('config.py').read())


# Project version number
__version__ = '0.0.1'


camera = PiCamera()
light_flash = LED(PIN_LIGHT_FLASH)
light_red = LED(PIN_LIGHT_RED)
light_yellow = LED(PIN_LIGHT_YELLOW)
light_green = LED(PIN_LIGHT_GREEN)


# 0. Init progress
def progress():
    print(bcolors.HEADER + '\n:::: PhArt – Start progress ::::\n' + bcolors.ENDC)
    # 1. Photo
    _preflash()
    file_name = _photo()
    # 2. Converting


# 1. **Photo**

# 1.1 Pulse() RED light
# 1.2 Blink flash light 3 times short


def _preflash():
    light_flash.on()
    sleep(.1)
    light_flash.off()
    sleep(1)
    light_flash.on()
    sleep(.1)
    light_flash.off()
    sleep(1)
    light_flash.on()
    sleep(.1)
    light_flash.off()
    sleep(1)

# 1.3 Take a photo with long flash light
# 1.4 Turn off flash light
# 1.5 Solid RED light


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def _photo():
    light_flash.on()
    sleep(2)
    ts = datetime.now().isoformat()
    file_path = './images/%s.jpg' % ts
    camera.capture(file_path)
    sleep(1)
    print("✅ 1. Photo created \033[3m\033[94m%s\033[0m" % file_path)
    light_flash.off()
    light_red.on()
    return ts


# 2. **Converting**
# 2.1 Pulse() YELLOW light
# 2.2 Convert it into paths
# 2.3 Solid YELLOW light


button = Button(PIN_BUTTON)
button.when_pressed = progress

pause()
