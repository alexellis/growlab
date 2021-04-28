Deploy faasd to your Raspberry Pi 3 or 4

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

