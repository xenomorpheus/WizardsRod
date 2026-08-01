"""hardware base class"""


class Hardware:
    """
    hardware base class.

    Hardware events are sent to listeners when hardware events occur.

    The hardware_type must match the trigger_type of the SpellTrigger that is used to activate a spell.

    Example.  Each listener will be called with the following.

    listener.recieve_event(RodEventButton(channel, now))



    """

    def __init__(self, hardware_type: str) -> None:
        self.hardware_type: str = hardware_type
        self.listeners: list = []
        """ a list of objects that have the recieve_event method """

    def get_hardware_type(self) -> str:
        """get the hardware_type"""
        return self.hardware_type

    def activate(self) -> None:
        """make hardware available"""

    def deactivate(self) -> None:
        """finish using hardware"""

    def listener_add(self, listener) -> None:
        """add a listener for button events"""
        self.listeners.append(listener)

    def listener_remove(self, listener) -> None:
        """remove a listener for button events"""
        self.listeners.remove(listener)
