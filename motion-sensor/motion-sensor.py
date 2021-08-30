#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

PIR_PIN = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')

while True:
  if GPIO.input(PIR_PIN):
    print('Motion Detected')
  time.sleep(1)
