from os import environ
from gpiozero import PWMLED
from brachiograph import BrachioGraph
from time import sleep
from vendor.BrachioGraph.linedraw import *


# 2. **Converting**
# 2.1 Pulse() YELLOW light
# 2.2 Convert it into paths
# 2.3 Solid YELLOW light

class Convert:
    def __init__(self, pin_led_status, image_name):
        print("Convert the photo to an image")
        self.led_status = PWMLED(pin_led_status)
        self.image_name = image_name
        self._render(self)
   
    def _render(self):
        self.led_status.pulse(.1)
        sleep(1)
        image_to_json(self.image_name, draw_contours=2, draw_hatch=16)
        self.led_status.value = .9
