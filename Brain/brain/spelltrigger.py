"""spell trigger"""

from brain.rodevent import RodEvent


class SpellTrigger:
    """Each trigger looks at events and determines if the trigger condition
    is met."""

    name = ""  # type: str
    spelltrigger_type = ""  # type: str

    def __init__(self, name: str, spelltrigger_type="none") -> None:
        self.name = name
        self.spelltrigger_type = spelltrigger_type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SpellTrigger):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.spelltrigger_type))

    def get_name(self) -> str:
        """get the name"""
        return self.name

    def get_spelltrigger_type(self) -> str:
        """get the spelltrigger_type"""
        return self.spelltrigger_type

    def is_triggerd_by(self, event: RodEvent) -> bool:
        """For simple triggers, the types just need to match."""
        return (issubclass(type(event), RodEvent)) and (
            self.get_name() == event.get_name() and self.get_spelltrigger_type() == event.get_event_type()
        )
