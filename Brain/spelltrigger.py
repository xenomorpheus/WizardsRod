from __future__ import absolute_import
from staffevent import StaffEvent

class SpellTrigger():

    def __init__(self, name):
        self.name = name

    def __key(self):
        return (self.name)

    def __eq__(self, other):
        return (type(self) is type(other)) and (self.getName() == other.getName())

    def __hash__(self):
        return hash(self.__key())

    def getName(self):
        return self.name

    def isTriggerdBy(self, event):
        """ For simple triggers, the event name just has to match. """
        return (issubclass(type(event), StaffEvent)) and (self.getName() == event.getName())
