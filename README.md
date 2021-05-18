# growlab

## A global contest to grow seeds and share your progress with the Raspberry Pi

![My green beans](https://pbs.twimg.com/media/Ey1ugNwWgAIyUiJ?format=jpg&name=small)
> A capture from phototimer of my seed tray with a wide-angle camera positioned above

## New Live stream - 27th April 16:30 BST

Got started already, or just want to learn more? Tune into the live stream [Grow your own with Raspberry Pi - Alex Ellis & Richard Gee](https://www.youtube.com/watch?v=Ta_LBKpI5-0)

## How it works

1) Read the launch blog post: [Join the Grow Lab Challenge](https://blog.alexellis.io/the-grow-lab-challenge/).
2) Order your kit, or decide you're taking part by sending a PR and adding yourself to the "growlab Technicians" section below.
3) Build your own `#growlab` using one of the designs, or customise it. And start growing and recording a timelapse.
4) Use the [#growlab hashtag](https://twitter.com/search?q=%23growlab&src=typed_query) and share as many pictures as you like.
5) Send a Pull Request and link to each Tweet to unlock each level.
6) At the conclusion of the growing period, we'll send some prizes from OpenFaaS Ltd and Pimoroni to entries at random for different tiers.

Prizes to be provided by: [OpenFaaS Ltd](https://openfaas.com) and [Pimoroni](https://www.pimoroni.com). Want to sponsor or provide prizes? Send an email to [alex@openfaas.com](mailto:alex@openfaas.com)

### Unlock each level

Before you get started with your build, send a PR to list yourself as a "lab technician".

Bronze - assemble your `#growlab` using one of the recommend designs or customise it. Tweet a photo of your build fully assembled.

Silver - install the software and capture your first photo of your seed tray or pots. Tweet the photo.

Gold - Wait until at least one of your seeds has germinated and grown into a seedling - around 2-3cm in height. Tweet the photo taken by the timelapse software.

Platinum - use the [phototimer](https://github.com/alexellis/phototimer) or seeds2 software to capture images over 14 days. Compile the images into a timelapse and upload it to YouTube. We recommend one photo every 10 minutes. Feel free to exclude any photos prior to the seeds germinating. Tweet a link to the video.

### Making your timelapse

If you're using phototimer, then you can run the following:

```bash
echo $(echo $(find ./Desktop/image/ | sort -V|grep jpg)) | xargs cat | ffmpeg  -framerate 10 -f image2pipe -vcodec mjpeg -i - -vcodec libx264 out.mp4
```

iMovie is also relatively easy to use, by dragging the images into the timeline and changing the time between images to ~ 0.1s

Here's a sample from 9th-22nd April you can watch on YouTube:

[![](https://img.youtube.com/vi/YiFUVAP0B18/hqdefault.jpg)](https://www.youtube.com/watch?v=YiFUVAP0B18)

[Click here](https://www.youtube.com/watch?v=YiFUVAP0B18) to watch my video timelapse

### Extra points and taking things further

![Self-watering system](https://pbs.twimg.com/media/EzZ1vDsXMAgNQKF?format=jpg&name=small)
> A self-watering system

* Overlay temperature and humidity data with a Bosch BME280 or BMP280 sensor
* Add a self-watering system with a small pump and capacitive soil sensor
* Try a garden RGB grow-light to give your seeds a little more help
* Experiment with hydroponics
* Install your lab in an outdoor greenhouse, shed or cold-frame
* Use a light sensor / LDR or UV sensor measure available light
* Try a suitable solar panel and battery capacity to run your experiment outdoors or in a room without a socket

## Growlab Technicians

Technicians work in laboratories, and you are no different, so if you've bought your kit, or have decided to join, then add your details below so that we can encourage each other and see how many people are participating. If you don't have a Twitter or GitHub handle just put N/a.

| # | Name                | Twitter         | GitHub        | Live preview URL |
|---|---------------------|-----------------|---------------|------------------|
| 1 | Alex Ellis | [@alexellisuk](https://twitter.com/alexellisuk) | [alexellis](https://github.com/alexellis)  | [Live preview with the growlab app](http://growlab.alexellis.io/) |
| 2 | Simon Emms | [@MrSimonEmms](https://twitter.com/MrSimonEmms)  | [MrSimonEmms](https://github.com/MrSimonEmms)  | [Images captured by phototimer](https://growlab.simonemms.com) |
| 3 | Richard Gee | [@rgee0](https://twitter.com/rgee0) | [rgee0](https://github.com/rgee0)  | [Most recently captured image](https://growlab.technologee.co.uk/) |
| 4 | Jakob Waibel | [@jakobwaibel](https://twitter.com/jakobwaibel) | [JakWai01](https://github.com/JakWai01) | [Live preview with the growlab app](https://jakwai01.github.io/growlab/)|
| 5 | Florian Clanet | [@FlolightC](https://twitter.com/FlolightC)  | [Flolight](https://github.com/Flolight) |
| 6 | Felix Pojtinger | [@pojntfx](https://twitter.com/pojntfx) | [pojntfx](https://github.com/pojntfx) |
| 7 | Sam Perrin | [@sam_perrin](https://twitter.com/sam_perrin) | [sam-perrin](https://github.com/sam-perrin) |
| 8 | Philippe Charrière | [@k33g_org](https://twitter.com/k33g_org) | [k33g](https://github.com/k33g) |
| 9 | John McCabe | [@mccabejohn](https://twitter.com/mccabejohn) | [johnmccabe](https://github.com/johnmccabe) ||
| 10 | Adam Craggs | [@abigpancake](https://twitter.com/abigpancake) | [agcraggs](https://github.com/agcraggs) |  |
| 11 | Martin Woodward | [@martinwoodward](https://twitter.com/martinwoodward) | [martinwoodward](https://github.com/martinwoodward) | [Live preview](https://bfaulty.z16.web.core.windows.net/) |
| 12 | Jérôme Velociter | [@jvelo](https://twitter.com/jvelo) | [jvelo](https://github.com/jvelo) |  |
| 13 | Philippe Ensarguet | [@p_ensarguet](https://twitter.com/P_Ensarguet) | [pensarguet](https://github.com/pensarguet) |  |
| 14 | Sander Vanhove | [@SanderWaylay](https://twitter.com/SanderWaylay) | [SanderVanhove](https://github.com/SanderVanhove) | [Live preview](https://www.sandervanhove.com/plant-monitor) |
| 15 | Sergei Vasilev | [@nblpblc](https://twitter.com/nblpblc) | [sergevas](https://github.com/sergevas) | |
| 16 | IbooNox | [@iboonox](https://twitter.com/iboonox) | [iboonox](https://github.com/iboonox) | |
| 17 | Allan Pead | [@adpead](https://twitter.com/adpead) | [apead](https://github.com/apead) | |
| 18 | Keith Hubner | [@keithhubner](https://twitter.com/keithhubner) | [keithhubner](https://github.com/keithhubner) | [Live preview](https://growlab.hubner.co.uk/) |
| 19 | Antoine Mouchere | [@mouchere_a](https://twitter.com/mouchere_a) | [amouchere](https://github.com/amouchere/growlab-project#readme) | [Live preview](https://amouchere.github.io/growlab-preview/) |


### Live preview URLs

A live preview URL keeps things interesting and lets the community get a view inside your lab.

See the new [growlab app](/app) for your Raspberry Pi

## Contest entries `#growlab` 🥇🥈🥉

| Name  | Bronze   | Silver   | Gold   | Platinum |
|-------|----------|----------|--------|----------|
| Alex Ellis        | [Bronze](https://twitter.com/alexellisuk/status/1380227185894690823)  |  [Silver](https://twitter.com/alexellisuk/status/1380227185894690823) | [Gold](https://twitter.com/alexellisuk/status1380417347861774337)  | [Platinum](https://www.youtube.com/watch?v=YiFUVAP0B18)  |
| Richard Gee       | [Bronze](https://twitter.com/rgee0/status/1383379807585521665)  | [Silver](https://twitter.com/rgee0/status/1383379805928759301)  | [Gold](https://twitter.com/rgee0/status/1384765411913355265)  | [Platinum](https://twitter.com/rgee0/status/1387777830914768901)  |
|  Simon Emms       | [Bronze](https://twitter.com/MrSimonEmms/status/1386361659187412996)  | [Silver](https://twitter.com/MrSimonEmms/status/1386361659187412996)  | [Gold](https://twitter.com/MrSimonEmms/status/1391832940225630212) | [Platinum](https://twitter.com/MrSimonEmms/status/1391832943170146313) |
|  Florian Clanet   | [Bronze](https://twitter.com/FlolightC/status/1384587367785369602) | [Silver](https://twitter.com/FlolightC/status/1383802323164561418) |   | |
|  Philippe Charrière       |   |   |   |
|  John McCabe   | [Bronze](https://twitter.com/mccabejohn/status/1387001148419227648) | | | |
| Adam Craggs |  |  |  |  |
| Jakob Waibel | [Bronze](https://twitter.com/jakobwaibel/status/1386372010658443265) | [Silver](https://twitter.com/jakobwaibel/status/1386372010658443265) | [Gold](https://twitter.com/jakobwaibel/status/1388894057955479554) | [Platinum](https://www.youtube.com/watch?v=z8sY37OlFrw) |
|  Sander Vanhove   | [Bronze](https://twitter.com/SanderWaylay/status/1391665619616026624?s=20) | | | |

## Official growlab app

* [phototimer - Record images for the timelapse contest](https://github.com/alexellis/phototimer)
* [app - Generate and upload a live-preview with sensor data growlab app](/app)
* [data-logger - Capture environment data and plot on a Grafana dashboard](/data-logger)

## Community projects and add-ons

* phototimer for capturing photos from the RPi camera for a timelapse: [alexellis/phototimer](https://github.com/alexellis/phototimer)
* Richard Gee's seeds2 repo for tweeting and capturing images: [rgee0/seeds2](https://github.com/rgee0/seeds2)
* Sam Perrin's seed-viewer for viewing the images captured with phototimer [sam-perrin/seed-viewer](https://github.com/sam-perrin/seed-viewer)
* Sander Vanhove's plant-monitor using Waylay: [SanderVanhove/plant-monitor](https://github.com/SanderVanhove/plant-monitor)
