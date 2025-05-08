
""" The Staff brings together the prepared spells and the hardware. """

from typing import List
from spell import Spell
from spelllistprepared import SpellListPrepared
from hardwarefetch import HardwareFetch


class Staff():

    """ The Staff brings together the prepared spells and the hardware. """

    name: str
    spell_list_prepared: SpellListPrepared
    hardware_hints: set
    hwf: HardwareFetch

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

    def __get_new_staff_events(self) -> List:
        """ "Poll hardware_hints hardware for events """
        events: List = []
        for hardware_hint in self.hardware_hints:
            hardware = self.hwf.get(hardware_hint)
            events.append(hardware.get_events())
        return events

    def run(self) -> None:
        """ looking for staff events to trigger spells  """
        loops = 2
        while loops > 1:
            self.spell_list_prepared.accept_events(
                self.__get_new_staff_events())
            for spell in self.spell_list_prepared.get_triggered_spells():
                spell.perform_actions(self)
            loops = loops - 1
