#!/usr/bin/env python3
"""

Inspired by https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
Using Pillow library http://python-pillow.org/
install PIL using the command "sudo apt-get install python-imaging" and run the following program.
It will print RGB values of the image. If the image is large redirect the output to a file using '>' later open the file to see RGB values


       ./sprite_print_stats.py


"""

from PIL import Image
from pprint import pprint

class SpritePrint:

    def __init__(self):
        pass

    def sprite_print_stats(self, filename): 

        SPRITE_WIDTH = 3
        im = Image.open(filename, 'r').convert('RGB')
        pix = im.load()
        width, height = im.size
        sprite_count = int(width / SPRITE_WIDTH)

        for sprite_idx in range(sprite_count):
            sprite_offset = sprite_idx * SPRITE_WIDTH
            red_max = 0
            green_max = 0
            blue_max = 0
            red_min = 100000
            green_min = 100000
            blue_min = 100000
            for x in range(SPRITE_WIDTH):
                for y in range(height):
                    # pprint ("x={}, y={}, RGB={}".format(x, y, pix[x, y]))
                    red, blue, green = pix[x + sprite_offset, y]
                    red_max = max(red, red_max)
                    green_max = max(green, green_max)
                    blue_max = max(blue, blue_max)
                    red_min = min(red, red_min)
                    green_min = min(green, green_min)
                    blue_min = min(blue, blue_min)
            print("Sprite=%d" % sprite_idx)
            pprint (" max RGB values r={}, g={}, b={}".format(red_max, green_max, blue_max))
            pprint (" min RGB values r={}, g={}, b={}".format(red_min, green_min, blue_min))

if __name__ == "__main__":
    FILENAME = 'sprite/fire_dark_3x100_18.png'  # image can be in gif jpeg or png format 
    sp = SpritePrint()
    sp = sp.sprite_print_stats(filename=FILENAME)
