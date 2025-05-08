from led_grid import LedGrid
from unicodedata import bidirectional


class KnightRider(LedGrid):
    """ The classic red dot moving side to side like KnightRider (and Cylons)
    is displayed on a LED grid. """

    eye_c = 0xFF0000  # red
    background_c = 0x000000  # black

    def init(self, strip, num_led):
        """This method is called to initialize a colour program.
        """
        self.height = self.get_y()
        self.width = self.get_x()
        self.eye_height = int(self.height * 0.15)  # 15 %
        self.remainder_height = self.height - self.eye_height

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):

        half_steps = int(num_steps_per_cycle / 2)

        offset = int(abs(half_steps - current_step) /
                     half_steps * self.remainder_height)
        offset_increasing = current_step >= half_steps

        for i in range(self.eye_height):
            self.set_line_y_rgb(strip, offset + i, self.eye_c)
        if (offset_increasing):
            self.set_line_y_rgb(strip, offset, self.background_c)
            self.set_line_y_rgb(strip, offset - 1, self.background_c)
        else:
            self.set_line_y_rgb(strip,
                                offset + self.eye_height, self.background_c)
            self.set_line_y_rgb(strip, offset + self.eye_height + 1,
                                self.background_c)

        return 1
