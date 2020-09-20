from datetime import datetime
from gpiozero import LED, PWMLED
from picamera import PiCamera
from time import sleep

# 1. **Photo**
# 1.1 Pulse() RED light
# 1.2 Blink flash light 3 times short
# 1.3 Take a photo with long flash light
# 1.4 Turn off flash light
# 1.5 Solid RED light


class Photo:
    def __init__(self, pin_led_flash, pin_led_status):
        print("Make a photo.")
        self.camera = PiCamera()
        self.led_flash = LED(pin_led_flash)
        self.led_status = PWMLED(pin_led_status)
        self._preflash(self)
        return self._make_photo(self)

    def _preflash(self):
        while True:
            self.led_flash.on()
            sleep(.1)
            self.led_flash.led.off()
            sleep(1)

    def _make_photo(self):
        file_name = datetime.now().isoformat()
        file_path = './images/%s.jpg' % file_name
        self.led_flash.on()
        self.led_status.pulse(.1)
        self.camera.capture(file_path)
        sleep(1)
        self.led_flash.off()
        self.led_status.value = .9
        return file_name
