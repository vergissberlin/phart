from os import environ
from gpiozero import PWMLED
from brachiograph import BrachioGraph
from time import sleep
from vendor.BrachioGraph import BrachioGraph

# 3. **Draw it**
# 3.1 Pulse() GREEN light
# 3.2 Draw it with the plotter
# 3.3 Solid GREEN light


class Draw:
    def __init__(self, pin_led_status, image_name):
        print("Draw the image")
        self.led_status = PWMLED(pin_led_status)
        self.image_name = image_name
        self._bg = BrachioGraph(
            inner_arm=os.environ.get('ARM_INNER') or 8,  # Upper arm length cm
            outer_arm=os.environ.get('ARM_OUTER') or 8,  # Underarm length cm
            # Coordinates drawing area
            bounds=(-8, 4, 4, 13),
            servo_1_degree_ms=-10,                       # Movement shoulder servo
            servo_2_degree_ms=10,                        # Movement elbow servo
            servo_1_centre=1500,                         # Middle position shoulder
            servo_2_centre=1500,                         # Middle position elbow
            pw_down=os.environ.get('PW_DOWN') or 1850,   # Position pin bottom
            pw_up=os.environ.get('PW_UP') or 1500,       # Position pin lifted
        )
        self._draw(self)

    def _draw(self):
        self.led_status.pulse(.1)
        sleep(1)
        self._bg.box()
        self._bg.plot_file('images/%s.json' % self.image_name)
        sleep(1)
        self.led_status.value = .9
