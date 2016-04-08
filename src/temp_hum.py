
import lib.grove_rgb_lcd as lcd
from lib import grovepi as grovepi

import random
import time
import json


class TempHum:
    def __init__(self):
        self.buzzer_pin = 8
        self.th_pin = 7
        self.sensor_version = 0

    def get_temp_hum(self):
        try:
            return grovepi.dht(self.th_pin, self.sensor_version)
        except (IOError, TypeError) as e:
            print "TempHum Read ERROR:", e
            return [0,0]

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
                [t, h] = self.get_temp_hum()
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

    def temp_hum_json(self):
        [t, h] = self.get_temp_hum()
        json_string = {"id:": "temp_hum", "data": [t, h], "pin": self.th_pin}
        return json.dump(json_string)

