#!/usr/bin/env python3
"""

Example of how to use the gesture event system.

Listen for POINTING_UPWARDS, LEANING_FORWARDS_UPWARDS, HORIZONTAL,
LEANING_FORWARDS_DOWNWARDS, and POINTING_DOWNWARDS.

"""

from __future__ import absolute_import
from brain.spell import Spell
from brain.rod import Rod
from brain.const import ST_GESTURE


class Main:  # pylint: disable=too-few-public-methods
    """Some examples to show how to call the code."""

    @staticmethod
    def spell_perform_action(spell, rod):
        """Perform the actions when the spell is triggered"""
        print("Perform Actions called on " + rod.name + " by spell " + spell.name)

    @staticmethod
    def _accelerator_example():
        """Accelerator example"""
        st_gesture = ST_GESTURE
        __fireball_trigger_sequence = [
            st_gesture["POINTING_UPWARDS"],
            st_gesture["LEANING_FORWARDS_UPWARDS"],
            st_gesture["HORIZONTAL"],
            st_gesture["LEANING_FORWARDS_DOWNWARDS"],
            st_gesture["POINTING_DOWNWARDS"],
        ]

        fireball = (
            Spell("Gesture Test")
            .set_trigger_sequence(__fireball_trigger_sequence)
            .set_trigger_timeout(6)
            .set_perform_action(Main.spell_perform_action)
        )
        rod = Rod("MyRod").spell_add(fireball)
        input("> press return to exit")
        rod.end()

    @staticmethod
    def main():
        """main"""
        Main._accelerator_example()


if __name__ == "__main__":
    Main.main()
