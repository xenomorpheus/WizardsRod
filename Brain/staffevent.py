

"""
An event that occurs on the staff.

"""


class StaffEvent():

    """

Events - Spells will be triggered by a sequence of these events.

* A button is pressed.
* A gesture/stamp of the staff
* A temperature change
* A pressure change
* Reaching a GPS location

    """

    def __init__(self, name: str, created) -> None:
        self.name = name
        self.created = created

    def __eq__(self, other: 'StaffEvent'):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.created))

    def get_name(self) -> str:
        return self.name

    def get_created(self):
        return self.created
