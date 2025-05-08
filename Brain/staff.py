
""" The Staff brings together the prepared spells and the hardware. """

from spell import Spell
from spelllistprepared import SpellListPrepared


class Staff():

    """ The Staff brings together the prepared spells and the hardware. """

    name: str
    spell_list_prepared: SpellListPrepared
    # hardware_hints: List(None)

    def __init__(self, name: str) -> None:
        self.name = name
        self.spell_list_prepared = SpellListPrepared(name + ' SpellListPrepared')
        self.hardware_hints = []

    def get_name(self) -> str:
        """ get the name """
        return self.name

    def spell_add(self, spell: Spell) -> 'Staff':
        """ add a spell to the prepared list """
        self.spell_list_prepared.spell_add(spell)
        self.__recalculate_hardware_hints()
        return self

    def spell_add_list(self, spelllist) -> 'Staff':
        """ add a list of spells to ghe prepared list """
        self.spell_list_prepared.spell_add_list(spelllist)
        self.__recalculate_hardware_hints()
        return self

    def __recalculate_hardware_hints(self) -> None:
        hardware_hints_new = self.spell_list_prepared.get_hardware_hints()
        # TODO add/remove hardware
        self.hardware_hints = hardware_hints_new

    def __get_new_staff_events(self):
        # TODO Poll hardware_hints hardware for events
        todo = self.hardware_hints
        return[]  # TODO

    def run(self) -> None:
        """ looking for staff events to trigger spells  """
        loops = 2
        while loops > 1:
            self.spell_list_prepared.accept_events(self.__get_new_staff_events())
            for spell in self.spell_list_prepared.get_triggered_spells():
                spell.performActions(self)
            loops = loops - 1
