# Technician onboarding

It's helpful to have an understanding of GPIO and i2c when building your growlab on a RPi.

The [GPIO](https://www.raspberrypi.org/documentation/hardware/raspberrypi/gpio/) (or **Genernal Purpose Input Output**) is a piece of hardware (pins) that allows your RPi to connect with real-world peripherals.

[i2c](https://en.wikipedia.org/wiki/I%C2%B2C) or **i squared c** is a [bus](https://en.wikipedia.org/wiki/Bus_%28computing%29) compatible with RPi using the GPIO pins. It shares data between peripherals connected to GPIO pins and the RPi.

Here is a brief walk-through for [enabling and using i2c on RPi](https://diyprojects.io/activate-i2c-bus-raspberry-pi-3-zero/).

## Connecting the GPIO pins to a RPi

RPi can be purchased with a GPIO connector that is loose (requiring you to solder it), soldered for you in advance, or be connected through solderless means. If you decide to buy a loose one and solder it yourself, but are new to soldering, [watch this video for some ideas](https://www.youtube.com/watch?v=8Z-2wPWGnqE).

## Connecting i2c peripherals to GPIO pins

Peripherals generally have a manual. Manuals describe how different pin configurations may control peripheral attributes. For example, a periphal may default to address 0x77, but can be configured to use 0x76.

For reference, [here are the pinouts for the 40-pin GPIO](https://www.raspberrypi.org/documentation/usage/gpio/images/GPIO-Pinout-Diagram-2.png).

## Get the i2c address of a connected peripheral

The below example shows you how to inspect the address associated with devices plugged into your RPi. It uses the `i2c-tools` package, which you must install to participate in growlab.

```bash
# list connected devices by address
i2cdetect -y 1
# sample output (here my BME280 is connected)
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- 76 --   
```

The peripheral's address is **76**, also referred to as **0x76**.

## Materials

You'll need a variety of [materials](materials.md), especially if you must solder GPIO pins. Checkout what other technicians have had success with, and add some of your own.
