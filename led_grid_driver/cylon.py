
from ledgridtemplate import LedGridTemplate

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


