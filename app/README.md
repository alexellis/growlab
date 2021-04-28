# `#growlab` app for Raspberry Pi

Create a timelapse with sensor data from a Bosch BME280 temperature, humidity and air pressure sensor.

## Assembling the build

* You'll need a Raspberry Pi Zero W or any other Raspberry Pi.
* A BME280 sensor connected to GND, VCC SDL and SCL.
* An RPi camera connected - any version

### Configuring the RPi

Using `raspi-config`

* Set your hostname such as `growpi`
* Enable i2c under interfacing options
* Change the password for the `pi` user

### Getting started with the software

Install git and tmux:

```bash
sudo apt update -qy && \
  sudo apt install -qy git tmux
```

Clone the repo:

```bash
git clone https://github.com/alexellis/growlab
cd growlab/app
```

Get the roboto font:

```bash
curl -sSL https://github.com/googlefonts/roboto/releases/download/v2.138/roboto-unhinted.zip -o roboto.zip
unzip roboto.zip -d roboto
```

Install apt packages:

```bash
sudo apt update -qy && \
  sudo apt install -qy python3 \
  python3-pip \
  libopenjp2-7 \
  libopenjp2-7-dev \
  libopenjp2-tools
```

The `libopenjp2` package is for overlaying text on top of the images.

Install Python modules with `pip3`:

```bash
sudo pip3 install -r requirements.txt
```

Capture a test image to determine if you need a horizontal or vertical flip or not:

```bash
# On the RPi
raspistill -o growlab.jpg

# From your PC:
scp pi@growlab.local:~/growlab.jpg Desktop/

# On a Mac:
open Desktop/growlab.jpg

# On a Linux desktop:
xdg-open Desktop/growlab.jpg
```

If needed, test again with `-vf` or `-hf` to flip the image.

Edit the `config.json` file if needed and update the flip settings, and width and height to match the file that you got from your test `growlab.jpg` image.

```json
{
    "images": {
        "output_dir": "./images/",
        "encoding": "jpeg",
        "width": 2592,
        "height": 1944,
        "image_quality": 70,
        "preview_seconds": 1,
        "vertical_flip": false,
        "horizontal_flip": false,
        "interval_seconds": 600
    },
    "text": {
        "colour": {
            "red": 255,
            "green": 255,
            "blue": 255
        },
        "size": 48
    }
}
```

Test the code:

```bash
python3 app.py
```

### Install growlab as a service

Install the systemd service:

```bash
touch /etc/default/growlab
sudo cp growlab.service /etc/systemd/system
sudo systemctl enable growlab
sudo systemctl start growlab
```
