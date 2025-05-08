
""" The Staff brings together the prepared spells and the hardware. """
from spell import Spell
from spelllistprepared import SpellListPrepared
from hardwarefetch import HardwareFetch


class Staff():

    """ The Staff brings together the prepared spells and the hardware. """

    def __init__(self, name: str) -> None:
        self.name = name
        self.spell_list_prepared = SpellListPrepared(self)
        """ a list of spells we are waiting for events in order to activate """
        self.hwf = HardwareFetch()
        """ object for fetching hardware interfaces """
        self.hardware = {}
        """ hardware interface objects. keyed by hardware hint string """

    def get_name(self) -> str:
        """ get the name """
        return self.name

    def spell_add(self, spell: Spell) -> 'Staff':
        """ add a spell to the prepared list """
        self.spell_list_prepared.spell_add(spell)
        self.__recalculate_hardware()
        return self

    def spell_add_list(self, spelllist) -> 'Staff':
        """ add a list of spells to the prepared list """
        self.spell_list_prepared.spell_add_list(spelllist)
        self.__recalculate_hardware()
        return self

    def __recalculate_hardware(self) -> None:
        hardware_hints_new = self.spell_list_prepared.get_hardware_hints()
        for hardware_hint in self.hardware.keys() - hardware_hints_new:
            self.hardware[hardware_hint].deactivate()
            del self.hardware[hardware_hint]
        for hardware_hint in hardware_hints_new - self.hardware.keys():
            hardware = self.hwf.get(hardware_hint)
            self.hardware[hardware_hint] = hardware
            hardware.activate()

    def end(self) -> 'Staff':
        """ shut down the hardware """
        for hardware_hint in list(self.hardware.keys()):
            self.hardware[hardware_hint].deactivate()
            del self.hardware[hardware_hint]
        return self

    def __del__(self):
        """ destructor """
        self.end()
