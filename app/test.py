from photo import Photo
from signal import pause
from time import sleep
from gpiozero import LED, Button

# Read the configuration
exec(open('config.py').read())


print("Welcome to Python on Docker (print)")

led_green = LED(PIN_LIGHT_GREEN)
led_yellow = LED(PIN_LIGHT_YELLOW)
led_red = LED(PIN_LIGHT_RED)
led_flash = LED(PIN_LIGHT_FLASH)
#
# while True:
#     led.on()
#     print('Light on')
#     sleep(1)
#     led.off()
#     print('Light off')
#     sleep(1)


# Read the configuration
exec(open('./config.py').read())

# Project version number
__version__ = '0.0.1'


def led_on():
    print("On!")
    led_green.on()
    led_yellow.on()
    led_red.on()
    led_flash.on()


def led_off():
    print("Off!")
    led_green.off()
    led_yellow.off()
    led_red.off()
    led_flash.off()


button = Button(PIN_BUTTON)
button.when_pressed = led_on
button.when_released = led_off

# image = Photo(PIN_OUTPUT_A, PIN_LIGHT_RED)
# print(image.file_name)

pause()
