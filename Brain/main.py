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
        hardware_hints = prepared_spells.getHardwareHints()

        staff = Staff()
        # only activate hardware sensors we are interested in
        staff.setHardwareHints(hardware_hints=hardware_hints)

        # looking for staff events to trigger spells
        loops = 2
        while loops > 1:
            new_staff_event_list = staff.getNewStaffEvents()
            prepared_spells.acceptEvents(new_staff_event_list)
            triggered_spells_list = prepared_spells.getTriggeredSpells()
            for spell in triggered_spells_list:
                spell.performActions(staff)
            loops = loops - 1


if __name__ == '__main__':
    main.main()