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

Bronze - assemble your `#growlab` using one of the recommend designs or customise it. Tweet a photo of your build.

Silver - install the software and capture your first photo of your seeds in the soil. Tweet it using the seeds2 software, or copy the file to your computer and Tweet it from there.

Gold - Wait until at least one of your seeds has germinated, and Tweet a second photo.

Platinum - use the [phototimer](https://github.com/alexellis/phototimer) or seeds2 software to capture images over a week. Compile the images into a timelapse and upload it to YouTube. We recommend one photo every 10 minutes. Tweet a link to the video.

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

* Overlay temperature and humidity data with an BME280 sensor
* Add a self-watering system with a small pump and capacitive soil sensor
* Try a garden RGB grow-light to give your seeds a little more help
* Experiment with hydroponics
* Install your lab in an outdoor greenhouse, shed or cold-frame
* Use a light sensor / LDR or UV sensor measure available light
* Try a suitable solar panel and battery capacity to run your experiment outdoors or in a room without a socket

## Growlab Technicians

Technicians work in laboratories, and you are no different, so if you've bought your kit, or have decided to join, then add your details below so that we can encourage each other and see how many people are participating. If you don't have a Twitter or GitHub handle just put N/a.

| Name                | Twitter         | GitHub        | Live preview URL |
|---------------------|-----------------|---------------|------------------|
| Alex Ellis | [@alexellisuk](https://twitter.com/alexellisuk) | [alexellis](https://github.com/alexellis)  | [Live preview with the growlab app](http://growlab.alexellis.io/) |
| Simon Emms | [@MrSimonEmms](https://twitter.com/MrSimonEmms)  | [MrSimonEmms](https://github.com/MrSimonEmms)  | [Images captured by phototimer](https://growlab.simonemms.com) |
| Richard Gee | [@rgee0](https://twitter.com/rgee0) | [rgee0](https://github.com/rgee0)  | [Most recently captured image](https://growlab.technologee.co.uk/) |
| Jakob Waibel | [@jakobwaibel](https://twitter.com/jakobwaibel) | [JakWai01](https://github.com/JakWai01) | [Live preview with the growlab app](https://jakwai01.github.io/growlab/)|
| Florian Clanet | [@FlolightC](https://twitter.com/FlolightC)  | [Flolight](https://github.com/Flolight) |
| Felix Pojtinger | [@pojntfx](https://twitter.com/pojntfx) | [pojntfx](https://github.com/pojntfx) |
| Sam Perrin | [@sam_perrin](https://twitter.com/sam_perrin) | [sam-perrin](https://github.com/sam-perrin) |
| Philippe Charrière | [@k33g_org](https://twitter.com/k33g_org) | [k33g](https://github.com/k33g) |
| John McCabe | [@mccabejohn](https://twitter.com/mccabejohn) | [johnmccabe](https://github.com/johnmccabe) ||
| Adam Craggs | [@abigpancake](https://twitter.com/abigpancake) | [agcraggs](https://github.com/agcraggs) |  |
| Martin Woodward | [@martinwoodward](https://twitter.com/martinwoodward) | [martinwoodward](https://github.com/martinwoodward) |  |

### Live preview URLs

A live preview URL keeps things interesting and lets the community get a view inside your lab.

See the new [growlab app](/app) for your Raspberry Pi

## Contest entries `#growlab` 🥇🥈🥉

| Name  | Bronze   | Silver   | Gold   | Platinum |
|-------|----------|----------|--------|----------|
| Alex Ellis        | [Bronze](https://twitter.com/alexellisuk/status/1380227185894690823)  |  [Silver](https://twitter.com/alexellisuk/status/1380227185894690823) | [Gold](https://twitter.com/alexellisuk/status1380417347861774337)  | [Platinum](https://www.youtube.com/watch?v=YiFUVAP0B18)  |
| Richard Gee       | [Bronze](https://twitter.com/rgee0/status/1383379807585521665)  | [Silver](https://twitter.com/rgee0/status/1383379805928759301)  | [Gold](https://twitter.com/rgee0/status/1384765411913355265)  |   |
|  Simon Emms       | [Bronze](https://twitter.com/MrSimonEmms/status/1386361659187412996)  | [Silver](https://twitter.com/MrSimonEmms/status/1386361659187412996)  |   |
|  Florian Clanet   | [Bronze](https://twitter.com/FlolightC/status/1384587367785369602) | [Silver](https://twitter.com/FlolightC/status/1383802323164561418) |   | |
|  Philippe Charrière       |   |   |   |
|  John McCabe   | [Bronze](https://twitter.com/mccabejohn/status/1387001148419227648) | | | |
| Adam Craggs |  |  |  |  |
| Jakob Waibel | [Bronze](https://twitter.com/jakobwaibel/status/1386372010658443265) | [Silver](https://twitter.com/jakobwaibel/status/1386372010658443265) | [Gold](https://twitter.com/jakobwaibel/status/1388894057955479554) | [Platinum](https://www.youtube.com/watch?v=z8sY37OlFrw) |

## Community projects and add-ons

* phototimer for capturing photos from the RPi camera for a timelapse: [alexellis/phototimer](https://github.com/alexellis/phototimer)
* Richard Gee's seeds2 repo for tweeting and capturing images: [rgee0/seeds2](https://github.com/rgee0/seeds2)
* Sam Perrin's seed-viewer for viewing the images captured with phototimer [sam-perrin/seed-viewer](https://github.com/sam-perrin/seed-viewer)
