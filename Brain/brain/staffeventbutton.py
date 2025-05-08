"""

Events - A button is pressed.

"""

from staffevent import StaffEvent


class StaffEventButton(StaffEvent):

    """ Events - A button is pressed.    """

    def __init__(self, name, created, type='BUTTON') -> None:
        super().__init__(name, created, type)
