""" spell trigger """

from staffevent import StaffEvent


class SpellTrigger():

    """ Each trigger looks at events and determines if the trigger condition
    is met. """


    def __init__(self, name: str, trigger_type='none') -> None:
        self.name = name
        self.trigger_type = trigger_type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SpellTrigger):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.trigger_type))

    def get_name(self) -> str:
        """ get the name """
        return self.name

    def get_trigger_type(self) -> str:
        """ get the trigger_type """
        return self.trigger_type

    def is_triggerd_by(self, event: StaffEvent):
        """ For simple triggers, the types just need to match. """
        return (issubclass(type(event), StaffEvent)) and (
            self.get_name() == event.get_name() and
            self.get_trigger_type() == event.get_event_type())
