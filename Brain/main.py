from __future__ import absolute_import
from const.spelltriggergestureconst import SpellTriggerGestureConst
from const.spellhardwareconst import SpellHardwareConst
from spell import Spell
from spelllistprepared import SpellListPrepared
from staff import Staff

class main():

    def main():
        fireball_trigger_sequence = [
            SpellTriggerGestureConst.Pointing_Upwards,
            SpellTriggerGestureConst.Leaning_Forwards_Upwards,
            SpellTriggerGestureConst.Horizontal,
            SpellTriggerGestureConst.Leaning_Forwards_Downwards,
            SpellTriggerGestureConst.Pointing_Downwards ]

        fireball = Spell("Fireball").setTriggerSequence(fireball_trigger_sequence).setTriggerTimeout(6). \
            setHardwareSet([SpellHardwareConst.ACCELEROMETER])
        Staff("MyStaff").spellAdd(fireball).run()

if __name__ == '__main__':
    main.main()
