from ledgridtemplate import LedGridTemplate

class Hal9000(LedGridTemplate):

    eye_c        = 0xFF0000 # red
    background_c = 0x000000 # black
    trim_c       = 0xFFFFFF # white
    letters_c    = 0xFFFFFF # white

    def init(self, strip, num_led):
        """This method is called to initialise a colour program."""

        height = self.get_y()
        width = self.get_x()
        start_y = int(height * 0.10)
        eye_y = int(height * 0.13)
        mid_y = int(height * 0.18)
        end_y = int(height * 0.22)

        # Top line
        self.set_line_y_rgb(strip, start_y, self.trim_c)

        # EYE
        self.set_xy_rgb(strip, int(width/2), eye_y,  self.eye_c)
        self.set_line_y_rgb(strip, eye_y+1, self.eye_c)
        self.set_line_y_rgb(strip, eye_y+2, self.eye_c)
        self.set_xy_rgb(strip, int(width/2), eye_y+3, self.eye_c)

        # Grill
        for y in range(mid_y,end_y):
            self.set_line_y_rgb(strip, y, self.trim_c)

        # HAL9000
        cursor = end_y + 9
        # H
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)
        cursor+=1
        self.set_line_y_rgb(strip, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)

        # A
        cursor+=2
        self.set_xy_rgb(strip, 1, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)
        cursor+=1
        self.set_line_y_rgb(strip, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)

        # L
        cursor+=2
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        cursor+=1
        self.set_line_y_rgb(strip, cursor, self.letters_c)

        # 9
        cursor+=2
        self.set_line_y_rgb(strip, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 0, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)
        cursor+=1
        self.set_line_y_rgb(strip, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)
        cursor+=1
        self.set_xy_rgb(strip, 1, cursor, self.letters_c)
        self.set_xy_rgb(strip, 2, cursor, self.letters_c)

        # 000
        for i in range(3):
            cursor+=2
            self.set_line_y_rgb(strip, cursor, self.letters_c)
            cursor+=1
            self.set_xy_rgb(strip, 0, cursor, self.letters_c)
            self.set_xy_rgb(strip, 2, cursor, self.letters_c)
            cursor+=1
            self.set_xy_rgb(strip, 0, cursor, self.letters_c)
            self.set_xy_rgb(strip, 2, cursor, self.letters_c)
            cursor+=1
            self.set_xy_rgb(strip, 0, cursor, self.letters_c)
            self.set_xy_rgb(strip, 2, cursor, self.letters_c)
            cursor+=1
            self.set_line_y_rgb(strip, cursor, self.letters_c)


    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # Do nothing: Init lit the strip, and update just keeps it this way
        return 0