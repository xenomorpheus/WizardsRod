"""

Events - A button is pressed.

"""

from time import gmtime
from staffevent import StaffEvent


class StaffEventButton(StaffEvent):

    """ Events - A button is pressed.    """

    def __init__(self, name, created=gmtime(), type='BUTTON') -> None:
        super().__init__(name, created, type)
