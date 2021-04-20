# growlab

![My green beans](https://pbs.twimg.com/media/Ey1ugNwWgAIyUiJ?format=jpg&name=small)
> My green beans are doing well

A global contest to grow seeds and share your progress with the Raspberry Pi

## How it works

1) Read the launch blog post: [Join the Grow Lab Challenge](https://blog.alexellis.io/the-grow-lab-challenge/).
2) Then build your own `#growlab` using one of the designs, or customise it. And start growing and recording a timelapse.
3) Use the [#growlab hashtag](https://twitter.com/search?q=%23growlab&src=typed_query) and share as many pictures as you like.
4) Send a Pull Request and link to each Tweet to unlock each level.
5) At the conclusion of the growing period, we'll send some prizes from OpenFaaS Ltd and Pimoroni to entries at random for different tiers.

Watch a [sample video here](https://www.youtube.com/watch?v=Y5rQD2eePY4)

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

## Community `#growlab`s 🥇🥈🥉

Ordered as seen on Twitter.

| Name  |Twitter   | Bronze   | Silver   | Gold   | Platinum |
|---|---|---|---|---|---|
| Alex Ellis  | [@alexellisuk](https://twitter.com/alexellisuk)  | [Bronze](https://twitter.com/alexellisuk/status/1380227185894690823)  |  [Silver](https://twitter.com/alexellisuk/status/1380227185894690823) | [Gold](https://twitter.com/alexellisuk/status1380417347861774337)  |   |
| Richard Gee  | [@rgee0](https://twitter.com/rgee0)  | [Bronze](https://twitter.com/rgee0/status/1383379807585521665)  | [Silver](https://twitter.com/rgee0/status/1383379805928759301)  | [Gold](https://twitter.com/rgee0/status/1384414687748673538)  |   |
|  Simon Emms | [@MrSimonEmms](https://twitter.com/MrSimonEmms)  |   |   |   |   |
|  Florian Clanet | [@FlolightC](https://twitter.com/FlolightC)  | [Bronze](https://twitter.com/FlolightC/status/1384587367785369602) | [Silver](https://twitter.com/FlolightC/status/1383802323164561418) |   |   |

