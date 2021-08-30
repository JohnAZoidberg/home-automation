#!/usr/bin/env python3

import time

import board
import adafruit_bh1750

def main():
    i2c = board.I2C()
    sensor = adafruit_bh1750.BH1750(i2c)

    while True:
        print(sensor.lux, "lux")
        time.sleep(1)

if __name__ == "__main__":
    main()
