from lib import grovepi as grovepi
import lib.grove_rgb_lcd as lcd
import sound_sensor as sound

import datetime
import time
import random
import json


class LightSensor:
    def __init__(self):
        self.sensor_pin = 1
        self.threshold = 10
        grovepi.pinMode(self.sensor_pin, "INPUT")
        self.sound = sound.SoundSensors()

    def get_sensor_data(self):
        try:
            sensor_value = grovepi.analogRead(self.sensor_pin)
            resistance = float((1023 - sensor_value) * 10 / sensor_value)
            print "LightSensor: %d, %.2f" %(sensor_value, resistance)
            return resistance
        except IOError as e:
            print "Error:LightSensor:", e

    def get_sensor_data_json(self):
        sensor_data = self.get_sensor_data()
        json_string = {"id:": "lightSensor", "data": sensor_data, "pin": self.sensor_pin}
        return json.load(json_string)

    def loop_it_baby(self, threshold=-99, buzzer=False):
        if threshold == -99:
            threshold = self.threshold
        while True:
            sensor_data = self.get_sensor_data()
            if sensor_data > threshold:
                if buzzer:
                    self.sound.buzz_it()
                    lcd.setRGB(240, 0, 0)
                    lcd.setText("Tooo much light: %s" %(str(sensor_data)))
                else:
                    (r, g, b) = self.get_rgb_combination(sensor_data)
                    lcd.setRGB(r, g, b)
                    lcd.setText("LightSensor: %s" %(str(sensor_data)))
            time.sleep(1)

    def get_rgb_combination(self, sensor_data):
        return (102, 178, 255)