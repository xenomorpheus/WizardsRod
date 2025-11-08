"""Spell"""

from typing import Callable, List, Optional, Set
from brain.spelltrigger import SpellTrigger

SpellTriggerSequence = List[SpellTrigger]


class Spell:
    """
    Spell - The definition of a spell.

    - Name
    - Trigger_Sequence
    - Trigger_Timeout
    - Hardware_Set

    Builder pattern.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        """ Name of the spell """
        self.trigger_sequence = []  # type: SpellTriggerSequence
        """ Ordered steps required to trigger the spell """
        self.reset_trigger_set = set()  # type: Set[SpellTrigger]
        """ TODO: Any of these spell triggers will abort every
             trigger sequence """
        self.trigger_timeout = 0  # type: int
        """ Maximum time to trigger the spell, from first trigger to last
        trigger. """
        self.perform_action = None  # type: Optional[Callable]
        """ code to call when trigger sequence completed """

    def __hash__(self):
        return hash(
            (
                self.name,
                tuple(self.trigger_sequence),
                tuple(self.reset_trigger_set),
                self.trigger_timeout,
                self.perform_action,
            )
        )

    def get_name(self) -> str:
        """get the name of the spell"""
        return self.name

    def set_trigger_sequence(self, trigger_sequence: SpellTriggerSequence) -> "Spell":
        """set the trigger sequence"""
        self.trigger_sequence = []
        for trigger in trigger_sequence:
            self.trigger_sequence.append(trigger)
        return self

    def get_trigger_sequence(self) -> SpellTriggerSequence:
        """get the trigger sequence"""
        return self.trigger_sequence

    def set_trigger_timeout(self, trigger_timeout: int) -> "Spell":
        """set the trigger timeout"""
        self.trigger_timeout = trigger_timeout
        return self

    def get_trigger_timeout(self):
        """get the trigger timeout"""
        return self.trigger_timeout

    def set_perform_action(self, perform_action: Optional[Callable] = None) -> "Spell":
        """set the method that is called when the spell run"""
        self.perform_action = perform_action
        return self

    def get_perform_action(self) -> Optional[Callable]:
        """get the method that is called when the spell run"""
        return self.perform_action
