#!/usr/bin/env python3
from datetime import datetime
import time

from PyP100 import PyP100
import RPi.GPIO as GPIO


# Configuration
PIR_PIN       = 23
p100_enable   = True
p100_range    = list(range(19, 25)) + list(range(0, 6)) # Only turn on light from 19:00 through 6:00
p100_timeout  = 60
p100_ip       = ""
p100_username = ""
p100_password = ""

def setup_motion_sensor_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)

def setup_p100():
    if p100_enable:
        print("Setting up and logging into P100")
    else:
        print("P100 is disabled")
        return

    p100 = PyP100.P100(p100_ip, p100_username, p100_password)

    # Creates the cookies required for further methods 
    p100.handshake()
    # Sends credentials to the plug and creates AES Key and IV for further methods
    p100.login()
    return p100

def switch_p100(p100, enable):
    if not p100_enable:
        return

    if enable:
        p100.turnOn()
    else:
        p100.turnOff()

def main():
    print("Setting up GPIO")
    setup_motion_sensor_gpio()
    p100 = setup_p100()

    timeout = 0

    print("Starting busyloop")
    while True:
        # Sleep one second between polling GPIO
        time.sleep(1)

        if timeout <= 0 and GPIO.input(PIR_PIN) and datetime.now().hour in p100_range:
            print("Motion Detected")
            # Turn on and keep on for a while
            timeout = p100_timeout
            switch_p100(p100, True)
            continue

        if timeout > 0 and timeout % 5 == 0:
            print(timeout)
        timeout -= 1
        if timeout == 0:
            print("Turning off again, timer ran out")
            switch_p100(p100, False)

if __name__ == "__main__":
    main()
