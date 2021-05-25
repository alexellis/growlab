try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
from bmp280 import BMP280
import bme680

import time

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

class growbme680:
    def __init__(self, oversample=True):
        self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
        self.oversample = oversample

    def get_readings(self):
        if self.oversample:
            print("Oversampling")
            self.sensor.set_humidity_oversample(bme680.OS_2X)
            self.sensor.set_pressure_oversample(bme680.OS_4X)
            self.sensor.set_temperature_oversample(bme680.OS_8X)
            self.sensor.set_filter(bme680.FILTER_SIZE_3)

        temperature = self.sensor.data.temperature
        pressure = self.sensor.data.pressure
        humidity = self.sensor.data.humidity
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity
        }
