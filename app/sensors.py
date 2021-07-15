try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
from bmp280 import BMP280

import time

class grownosensor:
    def __init__(self, date_format):
        self.date_format = date_format

    def get_readings(self):
        date_str = time.strftime(self.date_format)
        time_str = time.strftime("%H:%M:%S")

        return {
            "date": date_str,
            "time": time_str,
        }

class growbme280:
    def __init__(self, date_format):
        self.bus = SMBus(1)
        self.sensor = BME280(i2c_dev=self.bus)
        self.date_format = date_format

    def get_readings(self):
        # Ignore first result since it seems stale
        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        humidity = self.sensor.get_humidity()
        time.sleep(0.1)

        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        humidity = self.sensor.get_humidity()
        date_str = time.strftime(self.date_format)
        time_str = time.strftime("%H:%M:%S")

        return {
            "date": date_str,
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
        }

class growbmp280:
    def __init__(self, date_format):
        self.bus = SMBus(1)
        self.sensor = BMP280(i2c_dev=self.bus)
        self.date_format = date_format

    def get_readings(self):
        # Ignore first result since it seems stale
        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time.sleep(0.1)

        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        date_str = time.strftime(self.date_format)
        time_str = time.strftime("%H:%M:%S")

        return {
            "date": date_str,
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
        }
