#!/usr/bin/env python3
# Inspired by https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
# Using Pillow library http://python-pillow.org/
# install PIL using the command "sudo apt-get install python-imaging" and run the following program.
# It will print RGB values of the image. If the image is large redirect the output to a file using '>' later open the file to see RGB values

from PIL import Image
from pprint import pprint
from ledgridtemplate import LedGridTemplate
from unicodedata import bidirectional


class Sprite(LedGridTemplate):

    def init(self, strip, num_led):
        """This method is called to initialize a colour program.
        """

        FILENAME='lightning2 30x100.png' #image can be in gif jpeg or png format 
        im=Image.open(FILENAME, 'r').convert('RGB')
        self.pix=im.load()
        self.width = 3
        self.height = 100

        # width, height = im.size

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):

        sprite_offset = current_cycle * 3
        for x in range(self.width):
          for y in range(self.height):
            red, green, blue = self.pix[x+sprite_offset,y]
            self.set_pixel_xy(strip, x, y, red, green, blue)

        return 1
