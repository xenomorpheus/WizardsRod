"""
A specific Spell's definition.

"""

from typing import List, Callable
from spelltrigger import SpellTrigger
SpellTriggerSequence = List[SpellTrigger]


class Spell():

    """    Builder pattern.    """


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
        self.perform_actions_method = None

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

    def set_trigger_timeout(self, trigger_timeout: int) -> 'Spell':
        """ set the trigger timeout """
        self.trigger_timeout = trigger_timeout
        return self

    def get_trigger_timeout(self):
        """ get the trigger timeout """
        return self.trigger_timeout

    def set_hardware_set(self, hardware_set: set) -> 'Spell':
        """ set the hardware the spell will need """
        self.hardware_set = hardware_set
        return self

    def get_hardware_set(self) -> set:
        """ get the hardware the spell will need """
        return self.hardware_set

    def set_perform_actions(self, perform_actions: Callable) -> 'Spell':
        """ set the method that is called when the spell run """
        self.perform_actions_method = perform_actions
        return self

    def perform_actions(self, staff) -> 'Spell':
        """ the outcome of the spell. e.g. flash lights, make sounds. """
        self.perform_actions_method(self, staff)
        return self
