#!/usr/bin/env python

from lib import grovepi as grovepi
import lib.grove_rgb_lcd as lcd

import datetime
import time
import random
import json


class SoundSensors:
  def __init__(self):
    self.sound_sensor_pin = 0
    self.led_pin = 4
    self.display_pin = 7
    self.threshold_value = 50
    self.buzzer_pin = 8
    self.ultrasonic_pin = 3

  def loop_it_baby(self):
    while True:
      try:
        sound_data = open("sound_data.txt", "a+")
        sound_value = grovepi.analogRead(self.sound_sensor_pin)
        distance = self.get_ultrasonic()
        if sound_value > self.threshold_value:
          print "Sound: ", sound_value, str(datetime.datetime.now())
          grovepi.digitalWrite(self.led_pin, 1)
          sound_data.write("%s - %d\n" %(str(datetime.datetime.now()), sound_value))
          self.buzz_it()
          grovepi.digitalWrite(self.led_pin, 0)
        else:
          print "Sound output: ", sound_value, str(datetime.datetime.now())
          grovepi.digitalWrite(self.led_pin, 0)
          sound_data.write("%s --- LOW --- %d\n" %(str(datetime.datetime.now()), sound_value))
        lcd.setRGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        lcd.setText("Distance: %d" %(distance))
        time.sleep(5)
      except Exception, e:
        print str(e)

  def sound_json(self):
    sound_value = grovepi.analogRead(self.sound_sensor_pin)
    json_string = {"id:": "temp_hum", "data": sound_value, "pin": self.sound_sensor_pin}
    return json.load(json_string)

  def buzz_it(self, duration=1):
    grovepi.pinMode(self.buzzer_pin, "OUTPUT")
    grovepi.digitalWrite(self.buzzer_pin, 1)
    time.sleep(duration)
    grovepi.digitalWrite(self.buzzer_pin, 0)

  def get_ultrasonic(self, count=0):
    try:

      if count < 5:
        distance = grovepi.ultrasonicRead(self.ultrasonic_pin)
      else:
        return -99
      print "Distance: ", distance, str(datetime.datetime.now())
      return distance
    except (TypeError, IOError) as e:
      print "Error: Ultrasonic sensor ", e
      return self.get_ultrasonic(count+1)

  def get_ultrasonic_json(self):
    distance = self.get_ultrasonic()
    json_string = {"id:": "ultrasonic_sensor", "data": distance, "pin": self.sound_sensor_pin}
    return json.load(json_string)

  def disco(self):
    while True:
      lcd.setRGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      time.sleep(0.5)

