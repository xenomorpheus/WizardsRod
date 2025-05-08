#!/usr/bin/env python3
"""

Some examples to show how to call the code.

"""

from __future__ import absolute_import
import const
from spell import Spell
from staff import Staff


class Main():  # pylint: disable=too-few-public-methods
    """ Some examples to show how to call the code.  """

    @staticmethod
    def spell_perform_actions(spell, staff):
        """ Perform the actions when the spell is triggered """
        print("Perform Actions called on "+staff.name+" by spell "+spell.name)

    @staticmethod
    def _accelerator_example():
        """ Accelerator example """
        st_gesture = const.ST_GESTURE
        __fireball_trigger_sequence = [
            st_gesture['POINTING_UPWARDS'],
            st_gesture['LEANING_FORWARDS_UPWARDS'],
            st_gesture['HORIZONTAL'],
            st_gesture['LEANING_FORWARDS_DOWNWARDS'],
            st_gesture['POINTING_DOWNWARDS']]

        fireball = Spell("Gesture Test").set_trigger_sequence(
            __fireball_trigger_sequence).set_trigger_timeout(6). \
            set_hardware_set(set([const.HARDWARE["ACCELEROMETER"]])). \
            set_perform_actions(Main.spell_perform_actions)
        staff = Staff("MyStaff").spell_add(fireball)
        input("> press return to exit")
        staff.end()

    @staticmethod
    def _button_example():
        """ Button example """
        st_button = const.ST_BUTTON
        __fireball_trigger_sequence = [
            st_button['BUTTON1'],
            st_button['BUTTON2']]

        fireball = Spell("Button Test").set_trigger_sequence(
            __fireball_trigger_sequence).set_trigger_timeout(6). \
            set_hardware_set(set([const.HW_BUTTON])). \
            set_perform_actions(Main.spell_perform_actions)
        staff = Staff("MyStaff").spell_add(fireball)
        input("> Waiting for BUTTON1 then BUTTON2. Press return to exit")
        staff.end()

    @staticmethod
    def main():
        """ main """
        Main._button_example()


if __name__ == '__main__':
    Main.main()
