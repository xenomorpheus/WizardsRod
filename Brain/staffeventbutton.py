from staffevent import StaffEvent


"""

Events - A button is pressed.

"""


class StaffEventButton(StaffEvent):

    """ Events - A button is pressed.    """

    def __init__(self, name, created, event_type='button') -> None:
        super().__init__(name, created, event_type)
