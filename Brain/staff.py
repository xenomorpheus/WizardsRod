
""" The Staff brings together the prepared spells and the hardware. """

from spell import Spell
from spelllistprepared import SpellListPrepared
from hardwarefetch import HardwareFetch


class Staff():

    """ The Staff brings together the prepared spells and the hardware. """

    def __init__(self, name: str) -> None:
        self.name = name
        self.spell_list_prepared = SpellListPrepared(
            name + ' SpellListPrepared')
        self.hardware_hints = set()
        self.hwf = HardwareFetch()

    def get_name(self) -> str:
        """ get the name """
        return self.name

    def spell_add(self, spell: Spell) -> 'Staff':
        """ add a spell to the prepared list """
        self.spell_list_prepared.spell_add(spell)
        self.__recalculate_hardware_hints()
        return self

    def spell_add_list(self, spelllist) -> 'Staff':
        """ add a list of spells to the prepared list """
        self.spell_list_prepared.spell_add_list(spelllist)
        self.__recalculate_hardware_hints()
        return self

    def __recalculate_hardware_hints(self) -> None:
        hardware_hints_new = self.spell_list_prepared.get_hardware_hints()
        for hardware_hint in self.hardware_hints - hardware_hints_new:
            self.hwf.get(hardware_hint).deactivate()
        for hardware_hint in hardware_hints_new - self.hardware_hints:
            self.hwf.get(hardware_hint).activate()
        self.hardware_hints = hardware_hints_new
