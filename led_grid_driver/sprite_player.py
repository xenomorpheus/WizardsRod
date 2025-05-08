#!/usr/bin/env python3

from PIL import Image
from pprint import pprint
from led_grid import LedGrid
#from unicodedata import bidirectional


class SpritePlayer(LedGrid):
    """
     Draw onto a LED grid the contents of a sprite file.

     Using Pillow library http://python-pillow.org/
     Install PIL using the command "sudo apt-get install python-imaging" and run the following program.
    """

    def set_sprite_filename(self, filename):
        im = Image.open(filename, 'r').convert('RGB')
        self.pix = im.load()

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        width = self.get_x()
        height = self.get_y()
        sprite_offset = current_cycle * width
        for x in range(width):
          for y in range(height):
            red, blue, green = self.pix[x + sprite_offset, y]  #NOTE RGB swap
            self.set_pixel_xy(strip, x, y, red, green, blue)
        return 1
