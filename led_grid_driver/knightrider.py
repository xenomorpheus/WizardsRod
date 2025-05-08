from ledgridtemplate import LedGridTemplate
from unicodedata import bidirectional

class KnightRider(LedGridTemplate):

    eye_c = 0xFF0000  # red
    background_c = 0x000000  # black


    def init(self, strip, num_led):
        """This method is called to initialize a colour program.
        """

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):

        height = self.get_y()
        width = self.get_x()
        eye_height = int(height * 0.15)  # 15 %
        remainder_height = height - eye_height
        half_steps = int(num_steps_per_cycle / 2)

        offset = int(abs(half_steps - current_step) / half_steps * remainder_height)
        offset_increasing = current_step >= half_steps

        for i in range (eye_height):
            self.set_line_y_rgb(strip, offset + i, self.eye_c)
        if (offset_increasing):
            self.set_line_y_rgb(strip, offset, self.background_c)
            self.set_line_y_rgb(strip, offset - 1, self.background_c)
        else:
            self.set_line_y_rgb(strip, offset + eye_height, self.background_c)
            self.set_line_y_rgb(strip, offset + eye_height + 1, self.background_c)

        return 1
