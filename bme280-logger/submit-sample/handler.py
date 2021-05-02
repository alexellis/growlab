import json
import os
import time
from datetime import datetime
from influxdb import InfluxDBClient

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    # Parse NodeMCU data packet into JSON
    r = json.loads(req)

    influx_host = os.getenv("influx_host")
    influx_port = os.getenv("influx_port")
    influx_db = os.getenv("influx_db")

    influx_user = get_file("/var/openfaas/secrets/influx-user")
    influx_pass = get_file("/var/openfaas/secrets/influx-pass")
    
    client = InfluxDBClient(influx_host, influx_port, influx_user, influx_pass, influx_db)

    points = make_points(r)

    res = client.write_points(points)
    client.close()

    return json.dumps(res)

def get_file(path):
    v = ""
    with open(path) as f:
        v = f.read()
        f.close()
    return v.strip()

def make_points(r):
    tags = {"sensor": r["sensor"]}
    my_date = datetime.now()
    iso_time = my_date.isoformat()
    points = []

    points.append({
      "measurement": "temp",
      "tags":  tags,
      "time": iso_time,
      "fields": {
        "value": float(r["temperature"])
      }
     })

    if "cpu_temperature" in r:
        points.append({
          "measurement": "cpu_temperature",
          "tags":  tags,
          "time": iso_time,
          "fields": {
            "value": float(r["cpu_temperature"])
          }
     })

    if "humidity" in r:
        points.append({
              "measurement": "humidity",
              "tags":  tags,
              "time": iso_time,
              "fields": {
              "value": float(r["humidity"])
             }
            })

    if "pressure" in r:
        points.append({
              "measurement": "pressure",
              "tags":  tags,
              "time": iso_time,
              "fields": {
              "value": float(r["pressure"])
             }
            })

    return points
