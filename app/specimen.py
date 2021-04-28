from PIL import Image, ImageFont, ImageDraw
from jinja2 import Template
import time

class specimen:
    def __init__(self, text_config, image_config):
        self.text_config = text_config
        self.image_config = image_config

    def save_image(self, filename, image, readings):
        with open(filename, 'wb') as file:
            file.write(image.getvalue())

        msg = self.format(readings)

        img = Image.open(filename, "r").convert("RGBA")
        img_draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('roboto/Roboto-Regular.ttf', self.text_config["size"])
        colour = (self.text_config["colour"]["red"] ,self.text_config["colour"]["green"], self.text_config["colour"]["blue"])

        text_size = img_draw.textsize(msg, font)

        pos = (10, 20)
        bg_size = (text_size[0]+30, text_size[1]+50)
        bg_img = Image.new('RGBA', img.size, (0, 0, 0, 0))

        bg_draw = ImageDraw.Draw(bg_img)
        overlay_transparency = 100
        bg_draw.rectangle((pos[0], pos[1], bg_size[0], bg_size[1]), fill=(0, 0, 0, overlay_transparency), outline=(255, 255, 255))
        bg_draw.text(xy=(pos[0]+10, pos[1]+10), text=msg, fill=colour, font=font)

        bg_img.save("./alpha.png")
#        img.paste(bg_img, box=(0,0))
        out = Image.alpha_composite(img, bg_img)
        print("Saving {}..".format(filename))
        r = out.convert('RGB')
        r.save(filename, "JPEG")
        print("Saved {}..OK".format(filename))

    def format(self, readings):
        degree_symbol=u"\u00b0"
        return "#growlab - {}\nTemperature: {:05.2f}{}C \nPressure: {:05.2f}hPa \nHumidity: {:05.2f}%".format(readings["time"], readings["temperature"], degree_symbol, readings["pressure"], readings["humidity"])

    def save_html(self, input_filename, output_path, readings):
        img = Image.open(input_filename, "r")

        img = img.resize((int(self.image_config["width"]/2), int(self.image_config["height"]/2)), Image.ANTIALIAS)
        img.save(output_path+"/preview.jpg", "JPEG")

        template_text = ""
        with open("index.jinja", 'r') as file:
            template_text = file.read()

        template = Template(template_text)
        degree_symbol=u"\u00b0"
        vals = {}
        vals["time"] = readings["time"]
        vals["temperature"] = "{:05.2f}{}C".format(readings["temperature"], degree_symbol)
        vals["humidity"] = "{:05.2f}%".format(readings["humidity"])
        vals["pressure"] = "{:05.2f}hPa".format(readings["pressure"])
        vals["uid"] = "{}".format(time.time())

        html = template.render(vals)
        with open(output_path+"/index.html", "w") as html_file:
            html_file.write(html)
            print("Wrote {}..OK".format(output_path+"/index.html"))
