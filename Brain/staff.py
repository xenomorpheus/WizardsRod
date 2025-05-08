from spell import Spell
from spelllistprepared import SpellListPrepared

class Staff():

    def __init__(self, name: str) -> None:
        self.name = name
        self.spell_list_prepared = SpellListPrepared(name + ' SpellListPrepared')
        self.hardware_hints = []

    def getName(self) -> str:
        return self.name

    def spellAdd(self, spell: Spell) -> 'Staff':
        self.spell_list_prepared.spellAdd(spell)
        self.__recalculate_hardware_hints()
        return self

    def spellAddList(self, spelllist) -> 'Staff':
        self.spell_list_prepared.spellAddList(spelllist)
        self.__recalculate_hardware_hints()
        return self

    def __recalculate_hardware_hints(self) -> None:
        hardware_hints_new = self.spell_list_prepared.getHardwareHints()
        # TODO add/remove hardware
        self.hardware_hints = hardware_hints_new

    def __getNewStaffEvents(self):
        # TODO Poll hardware_hints hardware for events
        return[] # TODO


    def run(self) -> None:
        # looking for staff events to trigger spells
        loops = 2
        while loops > 1:
            self.spell_list_prepared.acceptEvents(self.__getNewStaffEvents())
            for spell in self.spell_list_prepared.getTriggeredSpells():
                spell.performActions(staff)
            loops = loops - 1