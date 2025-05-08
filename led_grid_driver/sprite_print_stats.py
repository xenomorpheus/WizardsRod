#!/usr/bin/env python3
"""

It will print RGB values of the image.

Inspired by https://stackoverflow.com/questions/138250/ \
       how-can-i-read-the-rgb-value-of-a-given-pixel-in-python

Using Pillow library http://python-pillow.org/
install PIL using the command "sudo apt-get install python-imaging"
and run the following program.


       ./sprite_print_stats.py


"""

from PIL import Image
from pprint import pprint
import argparse


class SpritePrint:

    def __init__(self):
        pass

    def sprite_print_stats(self, filename):

        SPRITE_WIDTH = 3
        im = Image.open(filename)
        rgb_img = im.convert('RGB')
        width, height = rgb_img.size
        sprite_count = int(width / SPRITE_WIDTH)
        print("width={},height={}, sprite_count={}".format(
            width, height, sprite_count))

        for sprite_idx in range(sprite_count):
            sprite_offset = sprite_idx * SPRITE_WIDTH
            print("Sprite={}, offset={}".format(sprite_idx, sprite_offset))
            red_max = 0
            green_max = 0
            blue_max = 0
            red_min = 100000
            green_min = 100000
            blue_min = 100000
            for x in range(SPRITE_WIDTH):
                for y in range(height):
                    rgb = rgb_img.getpixel((x + sprite_offset, y))
                    pprint("x={}, y={}, RGB={}".format(x, y, rgb))
                    red, blue, green = rgb
                    red_max = max(red, red_max)
                    green_max = max(green, green_max)
                    blue_max = max(blue, blue_max)
                    red_min = min(red, red_min)
                    green_min = min(green, green_min)
                    blue_min = min(blue, blue_min)
            pprint(" max RGB values r={}, g={}, b={}"
                   .format(red_max, green_max, blue_max))
            pprint(" min RGB values r={}, g={}, b={}"
                   .format(red_min, green_min, blue_min))


if __name__ == "__main__":

    sprite_filename = 'sprite/fire_dark_3x100_18.png'
    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #    "--mode",
    #    type=str,
    #    default="hsv",
    #    help="Mode (hsv, lab)")
    # parser.add_argument(
    #    "--save-dir",
    #    type=str,
    #    help="Save results to dir")
    parser.add_argument(
        "--sprite",
        type=str,
        default=None,
        help="filename of sprite to show")
    # parser.add_argument(
    #    "--batch",
    #    action="store_true",
    #    help="Run in batch mode, skipping wait for key",
    #    default=False)

    args = parser.parse_args()
    if args.sprite:
        sprite_filename = args.sprite
    # image can be in gif jpeg or png format
    sp = SpritePrint()
    sp = sp.sprite_print_stats(filename=sprite_filename)
