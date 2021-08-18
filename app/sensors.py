try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
from bmp280 import BMP280

import time
import serial
import json

class grownosensor:
    def __init__(self):
        pass

    def get_readings(self):
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
        }

class growbme280:
    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = BME280(i2c_dev=self.bus)

    def get_readings(self):
        # Ignore first result since it seems stale
        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        humidity = self.sensor.get_humidity()
        time.sleep(0.1)

        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        humidity = self.sensor.get_humidity()
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity
        }

class growbmp280:
    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = BMP280(i2c_dev=self.bus)

    def get_readings(self):
        # Ignore first result since it seems stale
        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time.sleep(0.1)

        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
        }

class growarduino:
    def __init__(self):
        self.uart = serial.Serial('/dev/ttyACM0') # make config
    
    def get_readings(self):
        # Ignore first result since it seems stale
        _tmp = self.uart.readline()
        time.sleep(0.1)
        _tmp = self.uart.readline()
        sense = json.loads(_tmp.decode('utf-8'))
        sense['time'] = time.strftime("%H:%M:%S")

        return {
            "time": sense['time'],
            "temperature": sense['temperature'],
            "pressure": sense['pressure'],
            "humidity": sense['humidity']
        }
