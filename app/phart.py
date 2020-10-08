from signal import pause
from gpiozero import Button
from photo import Photo
#from draw import Draw
#from convert import Convert


# Read the configuration
exec(open('config.py').read())

#from os import system
# system("pigpiod")

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

    def __init__(self, started=False):
        print("Welcome to PhArt!")
        self._started = started

    def progress(self):
        if self._started != True:
            self._started = True
            taskPhoto = Photo(PIN_LIGHT_FLASH, PIN_LIGHT_RED)
            print(taskPhoto.getFileName)
            #image = Convert(PIN_LIGHT_YELLOW, image_name)
            #draw = Draw(PIN_LIGHT_GREEN, image_name)
            self._started = False

    @staticmethod
    def say_hello():
        print("Hello!")


taskPhart = PhArt()
taskPhart.say_hello()
taskPhart.progress()


#button = Button(PIN_BUTTON)
#button.when_pressed = PhArt.say_hello()
#phart = PhArt()

# pause()
