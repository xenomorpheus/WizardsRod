"""
A specific Spell's definition.

"""

from typing import List
from spelltrigger import SpellTrigger
SpellTriggerSequence = List[SpellTrigger]


class Spell():

    """
    Builder pattern.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        """ Name of the spell """
        self.trigger_sequence = []
        """ Ordered steps required to trigger the spell """
        self.trigger_timeout = 0
        """ Maximum time to trigger the spell, from first trigger to last
        trigger. """
        self.hardware_set = []
        """ Some spells are triggered by hardware actions. e.g Buttons, GPS,
        Accelerometer """

    def get_name(self) -> str:
        """ get the name of the spell """
        return self.name

    def set_trigger_sequence(self, trigger_sequence: SpellTriggerSequence
                             ) -> 'Spell':
        """ set the trigger sequence """
        self.trigger_sequence = trigger_sequence
        return self

    def get_trigger_sequence(self) -> SpellTriggerSequence:
        """ get the trigger sequence """
        return self.trigger_sequence

    def set_trigger_timeout(self, trigger_timeout) -> 'Spell':
        """ set the trigger timeout """
        self.trigger_timeout = trigger_timeout
        return self

    def get_trigger_timeout(self):
        """ get the trigger timeout """
        return self.trigger_timeout

    def set_hardware_set(self, hardware_set) -> 'Spell':
        """ set the hardware the spell will need """
        self.hardware_set = hardware_set
        return self

    def get_hardware_set(self):
        """ get the hardware the spell will need """
        return self.hardware_set

    def perform_actions(self) -> 'Spell':
        """ the outcome of the spell. e.g. flash lights, make sounds. """
        # TODO stuff
        return self
