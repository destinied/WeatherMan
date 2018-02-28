#!/usr/bin/python


import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 20

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


if humidity is not None and temperature is not None:
    temp = (temperature * 1.8) + 32
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, humidity))
else:
    print('Failed to get reading. Try again!')
