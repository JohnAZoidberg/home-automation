#!/usr/bin/env python3

import time

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

thresholds = [50, 227, 318, 408, 503, 606, 696, 795, 881, 976, 1079, 1170]

def decode_uv_from_voltage(voltage):
    millivolt = voltage * 1000
    for uv_index, threshold in enumerate(thresholds):
        if millivolt < threshold:
            return uv_index

    return 12

def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P0)

    while True:
        uv_index = decode_uv_from_voltage(chan.voltage)
        print("UV index: {:2}, {:4.2f} mV".format(uv_index, chan.voltage * 1000))
        time.sleep(1)

if __name__ == "__main__":
    main()
