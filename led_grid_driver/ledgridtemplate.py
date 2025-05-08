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