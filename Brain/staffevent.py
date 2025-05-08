

"""
An event that occurs on the staff.

"""


class StaffEvent(object):

    """

Events - Spells will be triggered by a sequence of these events.

* A button is pressed.
* A gesture/stamp of the staff
* A temperature change
* A pressure change
* Reaching a GPS location

    """
    #name: str
    #created: int
    #event_type: str

    def __init__(self, name, created, event_type='none') -> None:
        self.name = name
        self.created = created
        self.event_type = event_type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StaffEvent):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.created, self.event_type))

    def get_name(self) -> str:
        """ get name """
        return self.name

    def get_created(self) -> int:
        """ get time/date event was created """
        return self.created

    def get_event_type(self) -> str:
        """ get event_type """
        return self.event_type
