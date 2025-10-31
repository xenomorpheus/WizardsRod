"""
An event that occurs on the rod.

"""

from time import gmtime


class RodEvent:
    """

    Events - Spells will be triggered by a sequence of these events.

    * A button is pressed.
    * A gesture/stamp of the rod
    * A temperature change
    * A pressure change
    * Reaching a GPS location

    Events are immutable

    """

    def __init__(self, name, created=gmtime(), rodevent_type="none") -> None:
        self.name = name
        self.created = created
        self.rodevent_type = rodevent_type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RodEvent):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.created, self.rodevent_type))

    def get_name(self) -> str:
        """get name"""
        return self.name

    def get_created(self) -> int:
        """get time/date event was created"""
        return self.created

    def get_rodevent_type(self) -> str:
        """get rodevent_type"""
        return self.rodevent_type
