#!/usr/bin/env python3

LED_PIN = 17

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
     GPIO.output(LED_PIN, True)
     time.sleep(1)
     GPIO.output(LED_PIN, False)
     time.sleep(1)

