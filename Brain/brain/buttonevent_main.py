#!/usr/bin/env python3
"""

Example code to show how to use the button event system.

Listen for BUTTON1 then BUTTON2.

"""

from __future__ import absolute_import
from brain.spell import Spell
from brain.staff import Staff
from brain.const import HW_BUTTON, ST_BUTTON


class Main:  # pylint: disable=too-few-public-methods
    """Some examples to show how to call the code."""

    @staticmethod
    def spell_perform_action(spell, staff):
        """Perform the actions when the spell is triggered"""
        print("Perform Actions called on " + staff.name + " by spell " + spell.name)

    @staticmethod
    def _button_example():
        """Button example"""
        st_button = ST_BUTTON
        __fireball_trigger_sequence = [st_button["BUTTON1"], st_button["BUTTON2"]]

        fireball = (
            Spell("Button Test")
            .set_trigger_sequence(__fireball_trigger_sequence)
            .set_trigger_timeout(6)
            .set_hardware_set(set([HW_BUTTON]))
            .set_perform_action(Main.spell_perform_action)
        )
        staff = Staff("MyStaff").spell_add(fireball)
        input("> Waiting for BUTTON1 then BUTTON2. Press return to exit")
        staff.end()

    @staticmethod
    def main():
        """main"""
        Main._button_example()


if __name__ == "__main__":
    Main.main()
