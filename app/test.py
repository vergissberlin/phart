from time import sleep
from gpiozero import LED


from photo import Photo


print("Welcome to Python on Docker (print)")

# led = LED(4)
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


image = Photo(PIN_OUTPUT_A, PIN_LIGHT_RED)
print(image.file_name)
