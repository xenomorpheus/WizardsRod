"""

Events - A button is pressed.

"""

from time import gmtime
from brain.rodevent import RodEvent


class RodEventButton(RodEvent):
    """Events - A button is pressed."""

    def __init__(self, name, created=gmtime(), event_type="BUTTON") -> None:
        super().__init__(name, created, event_type)
