"""

Some examples to show how to call the code.

"""

from __future__ import absolute_import
from const.spelltriggertypegestureconst import SpellTriggerTypeGestureConst as GestureType
from const.spellhardwareconst import SpellHardwareConst
from spelltrigger import SpellTrigger
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

        __fireball_trigger_sequence = [
            SpellTrigger(GestureType.Pointing_Upwards),
            SpellTrigger(GestureType.Leaning_Forwards_Upwards),
            SpellTrigger(GestureType.Horizontal),
            SpellTrigger(GestureType.Leaning_Forwards_Downwards),
            SpellTrigger(GestureType.Pointing_Downwards)]

        fireball = Spell("Fireball").set_trigger_sequence(__fireball_trigger_sequence).set_trigger_timeout(6). \
            set_hardware_set([SpellHardwareConst.ACCELEROMETER])
        Staff("MyStaff").spell_add(fireball).run()


if __name__ == '__main__':
    Main.main()
