#!/usr/bin/python3

import RPi.GPIO as GPIO
import time


def callback(sensor_pin):  
  if GPIO.input(sensor_pin):
    print("LED off")
  else:
    print("LED on")

GPIO.setmode(GPIO.BCM)

sensor_pin = 27
GPIO.setup(sensor_pin, GPIO.IN)

GPIO.add_event_detect(sensor_pin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sensor_pin, callback)

while True:
  time.sleep(0.1)
