from ledgridtemplate import LedGridTemplate

class KnightRider(LedGridTemplate):

    eye_c        = 0xFF0000 # red
    background_c = 0x000000 # black


    def init(self, strip, num_led):
        """This method is called to initialize a colour program.
        """

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):

        height = self.get_y()
        width  = self.get_x()
        eye_width = int(height * 0.15) # 15 %

        # TODO - Not finished
        offset = None
        if (current_step < (num_steps_per_cycle/2)):
            offset = current_step
        else:
            offset = height - eye_width - current_step
        self.set_line_y_rgb(strip, -1+offset, self.background_c)
        for y in range (eye_width):
            self.set_line_y_rgb(strip, y+offset, self.eye_c)
        self.set_line_y_rgb(strip, offset, self.background_c)
        self.set_line_y_rgb(strip, 1+offset, self.background_c)

        return 1