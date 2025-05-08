#!/usr/bin/env python3
# Inspired by https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
# Using Pillow library http://python-pillow.org/
# install PIL using the command "sudo apt-get install python-imaging" and run the following program.
# It will print RGB values of the image. If the image is large redirect the output to a file using '>' later open the file to see RGB values

from PIL import Image
from pprint import pprint
from ledgridtemplate import LedGridTemplate
from unicodedata import bidirectional


class SpritePlayer(LedGridTemplate):

    def set_sprite_filename(self, filename):
        im = Image.open(filename, 'r').convert('RGB')
        self.pix = im.load()
        # width, height = im.size

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):

        width = self.get_x()
        height = self.get_y()
        sprite_offset = current_cycle * width
        for x in range(width):
          for y in range(height):
            red, blue, green = self.pix[x + sprite_offset, y]  #NOTE RGB swap
            pprint (" MAX r={}, g={}, b={}".format(red, green, blue))
            #red = 10 * int(red / 10)
            #if red < 20 :
            #red = y
            #green = 10 * int(green / 10)
            #if green < 20 :
            #green = 0
            #blue = 10 * int(blue / 10)
            #if blue < 20 :
            #blue = 0
            self.set_pixel_xy(strip, x, y, red, green, blue)

        return 1
