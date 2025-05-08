""" spell trigger """

from staffevent import StaffEvent


class SpellTrigger():

    """ Each trigger looks at events and determines if the trigger condition
    is met. """
    name = ""  # type: str
    type = ""  # type: str

    def __init__(self, name: str, type='none') -> None:
        self.name = name
        self.type = type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SpellTrigger):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.type))

    def get_name(self) -> str:
        """ get the name """
        return self.name

    def get_type(self) -> str:
        """ get the type """
        return self.type

    def is_triggerd_by(self, event: StaffEvent) -> bool:
        """ For simple triggers, the types just need to match. """
        return (issubclass(type(event), StaffEvent)) and (
            self.get_name() == event.get_name() and
            self.get_type() == event.get_type())
