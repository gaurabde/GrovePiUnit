import random
import time

import lib.grove_rgb_lcd as lcd
from lib import grovepi as grovepi


class TestClass:
    def __init__(self):
        self.buzzer_pin = 8
        self.temp_sensor = 7
        self.sensor_version = 0

    def test_lcd(self):
        lcd.setText("test test")
        for code in range(0, 255):
            lcd.setRGB(code, 255 - code, 0)
            lcd.setText("ColorCode: %d, %d, %d" %(code, 255-code, 0))
            time.sleep(0.1)

    def temp_hum_loop(self):
        self.test_lcd()
        while True:
            try:
                [t, h] = grovepi.dht(self.temp_sensor, self.sensor_version)
                temp = str(t)
                hum = str(h)
                lcd.setRGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                print_string = "Temp: " + temp + " 'C" + " Hum: " + hum + "%"
                print print_string
                lcd.setText(print_string)
                grovepi.digitalWrite(self.buzzer_pin, 1)
                time.sleep(2)
                grovepi.digitalWrite(self.buzzer_pin, 0)
                time.sleep(60*10)
            except (IOError, TypeError) as e:
                print "Error: ", e
