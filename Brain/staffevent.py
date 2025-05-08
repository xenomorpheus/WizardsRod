

"""
An event that occurs on the staff.

"""

from spelltriggertype import SpellTriggerType


class StaffEvent():

    """

Events - Spells will be triggered by a sequence of these events.

* A button is pressed.
* A gesture/stamp of the staff
* A temperature change
* A pressure change
* Reaching a GPS location

    """
    event_type: SpellTriggerType

    def __init__(self, event_type, created) -> None:
        self.event_type = event_type
        self.created = created

    def __eq__(self, other: 'StaffEvent'):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.event_type, self.created))

    def get_event_type(self) -> str:
        """ get event_type """
        return self.event_type

    def get_created(self):
        """ get time/date event was created """
        return self.created
