"""

Some examples to show how to call the code.

"""

from __future__ import absolute_import
import const
from spell import Spell
from staff import Staff


class Main():  # pylint: disable=too-few-public-methods

    """

    Some examples to show how to call the code.

    """

    @staticmethod
    def main():

        """

        Some examples to show how to call the code.

        """
        st_gesture = const.ST_GESTURE
        __fireball_trigger_sequence = [
            st_gesture['POINTING_UPWARDS'],
            st_gesture['LEANING_FORWARDS_UPWARDS'],
            st_gesture['HORIZONTAL'],
            st_gesture['LEANING_FORWARDS_DOWNWARDS'],
            st_gesture['POINTING_DOWNWARDS']]

        fireball = Spell("Fireball").set_trigger_sequence(__fireball_trigger_sequence).set_trigger_timeout(6). \
            set_hardware_set([const.HARDWARE["ACCELEROMETER"]])
        Staff("MyStaff").spell_add(fireball).run()


if __name__ == '__main__':
    Main.main()
