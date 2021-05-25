import time
import os, json
from sensors import growbme280, growbmp280, growbme680
import requests
from datetime import datetime

function_url = os.getenv("FUNCTION_URL")  # change this on each Pi
sensor_name = os.getenv("SENSOR")
sample_duration = 30  # seconds

sensor = None
sensor_type = os.getenv("SENSOR_TYPE", "bme280")
print("Sensor type: {}", sensor_type)

if sensor_type == "bme280":
    sensor = growbme280()
if sensor_type == "bmp280":
    sensor = growbmp280()
elif sensor_type == "bme680":
    sensor = growbme680()

if function_url == None:
    sys.stderr.write("env-var FUNCTION_URL is required i.e. http://192.168.0.21:8080/function/submit-sample")
    os.exit(1)

if sensor_name == None:
    sys.stderr.write("env-var SENSOR is required i.e. shed1")
    os.exit(1)

def get_cpu_temp():
    path="/sys/class/thermal/thermal_zone0/temp"
    f = open(path, "r")
    temp_raw = int(f.read().strip())
    temp_cpu = float(temp_raw / 1000.0)
    return temp_cpu

try:
    while True:
        print("Gathering sensor data.")
        temp_cpu = get_cpu_temp()

        readings = sensor.get_readings()

        readings["sensor"] = sensor_name
        readings["cpu_temperature"] = temp_cpu

        my_date = datetime.now()
        readings["iso_time"] = my_date.isoformat()
        data = json.dumps(readings)
        print(data)

        try:
            res = requests.post(function_url, data=data, headers={"Content-type": "application/json"})
            if res.status_code != 200:
                print("Unexpected status code: {}".format(res.status_code))
            else:
                print("Sent to function..OK.")

        except Exception as e:
            print(e)
            continue
        time.sleep(sample_duration)

except KeyboardInterrupt:
    pass
