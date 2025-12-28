"""hardware base class"""

from typing import List


class Hardware:
    """
    hardware base class.

    Hardware events are sent to listeners when hardware events occur.

    Example.  Each listener will be called with the following.

    listener.recieve_event(RodEventButton(channel, now))

    """

    def __init__(self, name: str, hardware_type="none") -> None:
        self.name = name  # type: str
        self.hardware_type = hardware_type  # type: str
        self.listeners = []  # type: List
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
