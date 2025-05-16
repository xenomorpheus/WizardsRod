"""
Created on 19 Sep. 2019

@author: bruins
"""

from typing import List, Set

# Import Raspberry Pi GPIO library
try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils

    fake_rpigpio.utils.install()

from hardware import Hardware
from staffeventbutton import StaffEventButton


class ButtonEventGenerator(Hardware):
    """
    When hardware buttons are pressed send StaffEvent objects to
    listeners that have been previously setup.

    Example.  Each listener will be called with the following.

    listener.recieve_event(StaffEventButton(channel, now))

    """

    def __init__(self):
        """Constructor"""
        super().__init__(self)
        self.active = False  # type: bool
        self.channels = set()  # type: Set
        """ a list of button integers for the buttons """
        self.listeners = []  # type: List
        """ a list of objects that have the recieve_event method """

    def __hash__(self):
        return hash((self.active, self.channels, self.listeners))

    def listener_add(self, listener) -> None:
        """add a listener for button events"""
        self.listeners.append(listener)

    def listener_remove(self, listener) -> None:
        """remove a listener for button events"""
        self.listeners.remove(listener)

    def channel_add(self, channel: int) -> None:
        """add a button to those being listened to"""
        if not self.active:
            raise Exception("activate first")
        self.channels.add(channel)
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # Set pin channel to be an input pin and set initial value to be
        # pulled low (off).
        # Setup event on pin channel rising edge. Ignore further edges for
        # 200ms for switch bounce handling.
        # Multiple callback handlers can be added
        GPIO.add_event_detect(channel, GPIO.RISING, callback=self._button_callback, bouncetime=200)

    def channel_remove(self, channel: int) -> None:
        """remove a button from those being listened to"""
        self.channels.remove(channel)
        GPIO.remove_event_detect(channel)

    def activate(self) -> None:
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        self.active = True

    def deactivate(self) -> None:
        for channel in self.channels:
            self.channel_remove(channel)
        GPIO.cleanup()  # Clean up
        self.active = False

    def _button_callback(self, channel: int) -> None:
        print("Button {%d} was pushed!".format(channel))
        now = 0  # TODO
        event = StaffEventButton(str(channel), now)
        for listener in self.listeners:
            listener.recieve_event(event)
