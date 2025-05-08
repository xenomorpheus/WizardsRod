""" spell trigger """

from staffevent import StaffEvent
from spelltriggertype import SpellTriggerType

class SpellTrigger():

    """ Each trigger looks at events and determines if the trigger condition
    is met. """

    trigger_type: SpellTriggerType

    def __init__(self, trigger_type) -> None:
        self.trigger_type = trigger_type

    def __eq__(self, other: 'StaffEvent'):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.trigger_type))

    def get_name(self) -> str:
        return self.get_trigger_type().get_name()

    def get_trigger_type(self) -> SpellTriggerType:
        """ get the trigger_type """
        return self.trigger_type

    def is_triggerd_by(self, event: StaffEvent):
        """ For simple triggers, the types just need to match. """
        return (issubclass(type(event), StaffEvent)) and (
            self.get_trigger_type() == event.get_event_type())
