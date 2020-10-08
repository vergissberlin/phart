from datetime import datetime
from gpiozero import LED
from picamera import PiCamera
from time import sleep

# 1. **Photo**
# 1.1 Pulse() RED light
# 1.2 Blink flash light 3 times short
# 1.3 Take a photo with long flash light
# 1.4 Turn off flash light
# 1.5 Solid RED light


class Photo:

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    def __init__(self, pin_led_flash, pin_led_status):
        print("Make a photo.")
        self._camera = PiCamera()
        self._led_flash = LED(pin_led_flash)
        self._led_status = LED(pin_led_status)

        self._preflash()
        #
        #self.file_name = self._make_photo()

    def _preflash(self):
        while True:
            self._led_flash.on()
            sleep(.1)
            self._led_flash.off()
            sleep(1)
            self._led_flash.on()
            sleep(.1)
            self._led_flash.off()
            sleep(1)
            self._led_flash.on()
            sleep(.1)
            self._led_flash.off()
            sleep(1)
            break

    def _make_photo(self):
        self._file_name = datetime.now().isoformat()
        file_path = './images/%s.jpg' % self._file_name
        self._led_flash.on()
        self._led_status.blink()
        self._camera.capture(file_path)
        sleep(2)
        self._led_flash.off()
        self._led_status.off()

    @property
    def getFileName(self):
        return self._file_name
