"""

Example calling code

"""

from __future__ import absolute_import
from const.spelltriggergestureconst import SpellTriggerGestureConst
from const.spellhardwareconst import SpellHardwareConst
from spell import Spell
from staff import Staff

class Main():

    def main(self):
        fireball_trigger_sequence = [
            SpellTriggerGestureConst.Pointing_Upwards,
            SpellTriggerGestureConst.Leaning_Forwards_Upwards,
            SpellTriggerGestureConst.Horizontal,
            SpellTriggerGestureConst.Leaning_Forwards_Downwards,
            SpellTriggerGestureConst.Pointing_Downwards]

        fireball = Spell("Fireball").set_trigger_sequence(fireball_trigger_sequence). \
            set_trigger_timeout(6). \
            set_hardware_set([SpellHardwareConst.ACCELEROMETER])
        Staff("MyStaff").spell_add(fireball).run()

if __name__ == '__main__':
    main = Main()
    main.main()
