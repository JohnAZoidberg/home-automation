# Home Automation

- Display
  - Status: Working
  - Type: 1602
  - Pins: GND, VCC, SDA, SCL
  - Protocol: I2C
  - Script: display/i2clcd.py
  - [Tutorial](https://www.electroniclinic.com/raspberry-pi-16x2-lcd-i2c-interfacing-and-python-programming/)
- Motion Sensor
  - [Tutorial](https://www.freva.com/hc-sr501-pir-motion-sensor-on-raspberry-pi/)
  - Status: Working, sometimes triggers without movement (too sensitive)
  - Type: HC-SR501
  - Pins:
  - Script:
- Humidity Sensor
  - Type: DHT22
  - [Tutorial](https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/)
  - Pins: GND, DAT, VCC
- Light Intensity
  - Tutorial: https://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/
  - Protocol: I2C
  - Pins: 3V3, GND, SCL, SDA
