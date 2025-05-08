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

        # preparing a spell list
        prepared_spells = SpellListPrepared('MyList')
        prepared_spells.spellAddList([fireball])
        # prepared_spells.spellAdd(spell4)
        # prepared_spells.spellDel('spell name')

        # Some spells might need special hardware, e.g. GPS
        staff = Staff().setHardwareHints(prepared_spells.getHardwareHints())

        # looking for staff events to trigger spells
        loops = 2
        while loops > 1:
            prepared_spells.acceptEvents(staff.getNewStaffEvents())
            for spell in prepared_spells.getTriggeredSpells():
                spell.performActions(staff)
            loops = loops - 1


if __name__ == '__main__':
    main.main()
