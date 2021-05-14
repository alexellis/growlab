# BME280 Data Logger with faasd

This data logger writes measurements from a Bosch BME280 or BMP280 sensor into a InfluxDB time-series database.

## Deployment

You will run faasd on your Raspberry Pi 2, 3 or 4 to store data readings and to run OpenFaaS and Grafana.

On your Raspberry Pi Zero, or whichever host has a sensor connected to it, you'll run the sender app.

### Deploy faasd

Deploy faasd to your Raspberry Pi 3 or 4 [using these instructions](https://github.com/openfaas/faasd)

Customise the password, and update ` /var/lib/faasd/docker-compose.yaml`

```yaml
  influxdb:
    image: docker.io/library/influxdb:1.8
    environment:
      - INFLUXDB_DB=defaultdb
      - INFLUXDB_ADMIN_USER=admin
      - "INFLUXDB_ADMIN_PASSWORD=PASSWORD"
      - INFLUXDB_USER=user
      - "INFLUXDB_USER_PASSWORD=PASSWORD"
      - INFLUXDB_REPORTING_DISABLED=true
      - INFLUXDB_HTTP_AUTH_ENABLED=true
      - INFLUXDB_HTTP_BIND_ADDRESS=0.0.0.0:8086
    volumes:
      # we assume cwd == /var/lib/faasd
      - type: bind
        source: ./influxdb/
        target: /var/lib/influxdb
    user: "1000" 
    cap_add:
      - CAP_NET_RAW
    ports:
      - "0.0.0.0:8086:8086"
```

Make a directory for InfluxDB:

```bash
mkdir -p /var/lib/faasd/influxdb
chown 1000:1000 /var/lib/faasd/influxdb
```

Then reload and restart:

```bash
sudo systemctl daemon-reload \
  && sudo systemctl restart faasd
```

### Deploy the function

Create a secret for the InfluxDB user:

```bash
export PASSWORD=""

faas-cli secret create influx-password --from-literal $PASSWORD
faas-cli secret create influx-user --from-literal admin
```

Set the influx_db env-var in `stack.yml` i.e. `192.168.0.21`

Next, deploy the function:

```bash
faas-cli deploy
```

Build if you like:

```bash
faas-cli publish -f stack.yml --platforms linux/arm/7
```

### Deploy the sender onto your Raspberry Pi with a sensor

On your Raspberry Pi with the sensor, you'll run the "sender" app. You will need to run through the pre-reqs for the main growlab app, which enables the sensor and updates Python etc.

Copy the `sender` folder to your Raspberry Pi.

Install any pip modules:

```bash
pip3 install -r requirements.txt
```

Then run the sender app:

```bash
FUNCTION_URL=http://192.168.0.21:8080/function/submit-sample \
  SENSOR=my-shed \
  python3 main.py
```

> Note: if you're using a BMP280 sensor then add an addition environment variable of `SENSOR=bmp280`

A sensor reading will be submitted to faasd every 30 seconds. You can alter this sample interval by editing [sender/main.py](sender/main.py).

## Going further with a dashboard

Deploy Grafana to faasd using the instructions in the [eBook Serverless For Everyone Else](https://gumroad.com/l/serverless-for-everyone-else)

Then create yourself a simple dashboard for the measurements you see in the "readings" database.

Once you have it up and running, create a datasource, then import the dashboard.json file and open the dashboard to view your sensor readings.

![A very cold shed](https://pbs.twimg.com/media/E0H6WhfXIAAMOR3?format=jpg&name=medium)
> My very cold shed - measured overnight!

