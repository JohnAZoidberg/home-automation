#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
while True:
    print("Turning on")
    GPIO.output(17, True)
    time.sleep(10)

    print("Turning off")
    GPIO.output(17, False)
    time.sleep(2)

