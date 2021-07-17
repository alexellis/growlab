# BME280 Data Logger with faasd

This data logger writes measurements from a Bosch BME280 or BMP280 sensor into a InfluxDB time-series database.

You'll need one Raspberry Pi 3 or 4 to run the data collection stack and dashboard, then as many additional Raspberry Pi Zeros as you like for each location you want to monitor.

## The hardware

![How to connect the sensor over i2c](../app/sensor-i2c.png)
> How to connect the sensor over i2c

For the hardware, follow the instructions from the [growlab app](../app/) under "Assembling the build". You'll need the same parts, but you can skip the camera module.

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

faas-cli secret create influx-pass --from-literal $PASSWORD
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

On your Raspberry Pi with the sensor, you'll run the "sender" app.

Enable i2c and change the hostname as required using the `raspi-config` tool.

If you haven't installed the main growlab app for live-previews, then install the below dependencies:

```bash
sudo apt update -qy && \
  sudo apt install -qy python3 \
  i2c-tools \
  python3-pip \
  git \
  tmux
```

Clone the growlab app:

```bash
git clone https://github.com/alexellis/growlab
cd growlab/data-logger/sender/
```

Install any pip modules required for the sender app:

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

A larger version in the summer time:

![Getting very warm in my shed](https://pbs.twimg.com/media/E6feyrJWYAMc4l2?format=jpg&name=large)
