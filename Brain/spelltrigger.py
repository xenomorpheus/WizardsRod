from __future__ import absolute_import
from staffevent import StaffEvent


class SpellTrigger():

    def __init__(self, name: str) -> None:
        self.name = name

    def __key(self) -> str:
        return (self.name)

    def __eq__(self, other: 'SpellTrigger'):
        return (type(self) is type(other)) and (self.get_name() == other.get_name())

    def __hash__(self):
        return hash(self.__key())

    def get_name(self) -> str:
        return self.name

    def is_triggerd_by(self, event: StaffEvent):
        """ For simple triggers, the event name just has to match. """
        return (issubclass(type(event), StaffEvent)) and (self.get_name() == event.get_name())
