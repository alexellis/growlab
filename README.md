# growlab

A global contest to grow seeds and share your progress with the Raspberry Pi

![My green beans](https://pbs.twimg.com/media/Ey1ugNwWgAIyUiJ?format=jpg&name=small)
> My green beans are doing well

## How it works

Build your own [Grow Lab](https://blog.alexellis.io/the-grow-lab-challenge/) and particpate in the challenge

Use the [#growlab hashtag](https://twitter.com/search?q=%23growlab&src=typed_query) and share as many pictures as you like.

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

## Community `#growlab`s 🥇🥈🥉

Ordered as seen on Twitter.

| Name  |Twitter   | Bronze   | Silver   | Gold   | Platinum |
|---|---|---|---|---|---|
| Alex Ellis  | [@alexellisuk](https://twitter.com/alexellisuk)  | [Bronze](https://twitter.com/alexellisuk/status/1380227185894690823)  |  [Silver](https://twitter.com/alexellisuk/status/1380227185894690823) | [Gold](https://twitter.com/alexellisuk/status1380417347861774337)  |   |
| Richard Gee  | [@rgee0](https://twitter.com/rgee0)  | [Bronze](https://twitter.com/rgee0/status/1383379807585521665)  | [Silver](https://twitter.com/rgee0/status/1383379805928759301)  | [Gold](https://twitter.com/rgee0/status/1384414687748673538)  |   |
|  Simon Emms | [@MrSimonEmms](https://twitter.com/MrSimonEmms)  |   |   |   |   |


