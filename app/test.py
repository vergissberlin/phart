from time import sleep
from gpiozero import LED
import logging

# from os import system
# system("pigpiod")

logging.debug("Welcome to Python on Docker")

led = LED(4)

while True:
    led.on()
    print('Light on')
    sleep(1)
    led.off()
    print('Light off')
    sleep(1)
