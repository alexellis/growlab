# Growlab materials

Below is a variety of materials technicians have opted to use as part of growlab.

Please consider adding to this list once you've had success with a material, including any special tips.

## RPi

* [Vilros Raspberry Pi Zero W Basic Starter Kit](https://www.amazon.com/gp/product/B0748MPQT4), is a good starter kit. It'll require you to (1) solder the GPIO to the RPI and (2) purchase a separate micro SD card.

## Soldering

* [Tilswall Soldering Station](https://www.amazon.com/gp/product/B07XG1PD6D/), is a little pricy, but provides an adjustable, consistent heat, as well as a convenient cleaning ball for the soldering tip.

### Before soldering

* Prevent your RPi from moving before you solder by [sticking it to a surface with some mounting putty](https://www.amazon.com/gp/product/B001F57ZPW/).

### Solder wire

* If you must solder (for example, to connect a GPIO to a RPi), consider using [solder wire that is ~0.5mm thick](https://www.amazon.com/gp/product/B0759WKH3H/). Thin solder helps avoid mistakes that require a [desoldering wick](https://www.amazon.com/gp/product/B01N1EZNVF/).

## Cameras

* [Arducam Day & Night Vision for Raspberry Pi Camera with Holder](https://www.amazon.com/gp/product/B0834XSLZM/), is a little pricy, but has a mount and takes pictures in the dark using supporting IR LEDs. If you're interested in taking time lapse photos in the dark to see how plants move, check it out!

## BME280 sensors

There are a variety of makers for the BME280. The Bosch BME280 is preferred, but, there are other options too.

### Waveshare BME280

The `pimoroni-bme280` driver in the growlab app expects the BME280 to have an address of **0x76**. However, the Waveshare BME280 defaults to **0x77**. Connect the ADDR wire to a `GND` or ground pin and it'll use an address of **0x76**.

* [Purchase](https://www.amazon.com/Waveshare-Environmental-Temperature-Barometric-Detection/dp/B07P4CWGGK)
* [Download the manual](https://www.waveshare.com/w/upload/7/75/BME280_Environmental_Sensor_User_Manual_EN.pdf)
