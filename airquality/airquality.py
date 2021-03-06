#!/usr/bin/python
import serial, time, os
from Adafruit_IO import Client
aio = Client(os.environ.get('IO_USERNAME'), os.environ.get('IO_KEY'))

ser = serial.Serial('/dev/ttyUSB0')

while True:
        data = []
        for index in range (0,10):
                datum = ser.read()
                data.append(datum)

        pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
        aio.send('airquality25pm', pmtwofive)
        pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
        aio.send('airquality10pm', pmten)
        time.sleep(10)
