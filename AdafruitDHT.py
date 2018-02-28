#!/usr/bin/python
import sys

import Adafruit_DHT


sensor_args = { '11': Adafruit_DHT.DHT11}
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py 11 GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 11 20')
    sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    temp = (temperature * 1.8) + 32
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temp, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
