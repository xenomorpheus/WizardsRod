from colorcycletemplate import ColorCycleTemplate

class LedGridTemplate(ColorCycleTemplate):
    """ convert (x,y) into absolute pixel on a single strip.
    Left top corner is (0,0).
    The grid is formed by a taking a single strip and folding
    into a snake pattern, starting on the right, and always
    folding to the left.  """

    strip = None
    x_size = 0
    y_size = 0

    def set_x(self, x_size):
        self.x_size = x_size

    def get_x(self):
        return self.x_size

    def set_y(self, y_size ):
        self.y_size = y_size

    def get_y(self):
        return self.y_size

    def __to_pixel(self, x, y):
        """ convert (x,y) into absolute pixel.
        Left top corner is (0,0)
        The grid is formed by a snake pattern, starting on the
        right, and folding left.  """
        pixel = (self.x_size - 1 - x) * self.y_size
        if (x % 2 == 0 ):
            pixel += y
        else:
            pixel += self.y_size - 1 - y
        #print ("x={}, y={}, pixel={}".format(x,y, pixel))
        return pixel

    def set_xy_rgb(self, strip, x, y, colour):
        strip.set_pixel_rgb(self.__to_pixel(x, y), colour)

    def set_line_x_rgb(self, strip, x, colour):
        for y in range(self.y_size):
            strip.set_pixel_rgb(self.__to_pixel(x, y), colour)

    def set_line_y_rgb(self, strip, y, colour):
        for x in range(self.x_size):
            strip.set_pixel_rgb(self.__to_pixel(x, y), colour)


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
        eye_y = int(height * 0.14)
        mid_y = int(height * 0.18)
        end_y = int(height * 0.22)

        # Top line
        self.set_line_y_rgb(strip, start_y, self.trim_c)

        # EYE
        self.set_xy_rgb(strip, int(width/2), eye_y-1,  self.eye_c)
        self.set_line_y_rgb(strip, eye_y, self.eye_c)
        self.set_line_y_rgb(strip, eye_y+1, self.eye_c)
        self.set_xy_rgb(strip, int(width/2), eye_y+2, self.eye_c)

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

class Cylon(LedGridTemplate):

    eye_c        = 0xFF0000 # red
    background_c = 0x000000 # black


    def init(self, strip, num_led):
        """This method is called to initialize a colour program.
        """
        pass

    def update(self, strip, num_led, num_steps_per_cycle, current_step,
               current_cycle):
        # TODO
        height = self.get_y()
        width = self.get_x()
        return 1


