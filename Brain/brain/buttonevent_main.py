#!/usr/bin/env python3
"""

Example code to show how to use the button event system.

Listen for BUTTON1 then BUTTON2.

"""

from __future__ import absolute_import
from brain.spell import Spell
from brain.rod import Rod
from brain.const import ST_BUTTON


class Main:  # pylint: disable=too-few-public-methods
    """Some examples to show how to call the code."""

    @staticmethod
    def spell_perform_action(spell, rod):
        """Perform the actions when the spell is triggered"""
        print("Perform Actions called on " + rod.name + " by spell " + spell.name)

    @staticmethod
    def _button_example():
        """Button example"""
        fireball = (
            Spell("Button Test")
            .set_trigger_sequence([ST_BUTTON["BUTTON1"], ST_BUTTON["BUTTON2"]])
            .set_trigger_timeout(6)
            .set_perform_action(Main.spell_perform_action)
        )
        rod = Rod("MyRod").spell_add(fireball)
        input("> Waiting for BUTTON1 then BUTTON2. Press return to exit")
        rod.end()

    @staticmethod
    def main():
        """main"""
        Main._button_example()


if __name__ == "__main__":
    Main.main()
