"""
The definition of a spell.

- Name
- Trigger_Sequence
- Trigger_Timeout
- Hardware_Set

"""

from typing import Callable, List, Optional, Set
from spelltrigger import SpellTrigger
from hardware import Hardware

SpellTriggerSequence = List[SpellTrigger]


class Spell:
    """Builder pattern."""

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
        self.hardware_set = set()  # type: Set[Hardware]
        """ Some spells are triggered by hardware actions. e.g Buttons, GPS,
        Accelerometer """
        self.perform_actions = []  # type: Optional[List[Callable]]
        """ code to call when trigger sequence completed """

    def __hash__(self):
        return hash(
            (
                self.name,
                tuple(self.trigger_sequence),
                tuple(self.reset_trigger_set),
                self.trigger_timeout,
                tuple(self.hardware_set),
                self.perform_actions,
            )
        )

    def get_name(self) -> str:
        """get the name of the spell"""
        return self.name

    def print(self) -> "Spell":
        """TODO remove. print the spell"""
        print("spell " + self.name)
        for trigger in self.trigger_sequence:
            print(trigger.get_name())
        return self

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

    def set_hardware_set(self, hardware_set: set) -> "Spell":
        """set the hardware the spell will need"""
        self.hardware_set = set()
        for hardware in hardware_set:
            self.hardware_set.add(hardware)
        return self

    def get_hardware_set(self) -> set:
        """get the hardware the spell will need"""
        return self.hardware_set

    def set_perform_actions(self, perform_actions: Optional[List[Callable]] = None) -> "Spell":
        """set the method that is called when the spell run"""
        self.perform_actions = perform_actions
        return self

    def get_perform_actions(self) -> Optional[List[Callable]]:
        """get the method that is called when the spell run"""
        return self.perform_actions
