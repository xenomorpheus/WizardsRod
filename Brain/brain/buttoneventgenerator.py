"""
ButtonEventGenerator
"""

from typing import Set

# Import Raspberry Pi GPIO library
try:
    from RPi import GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils

    fake_rpigpio.utils.install()

from brain.hardware import Hardware
from brain.rodeventbutton import RodEventButton


class ButtonEventGenerator(Hardware):
    """
    When hardware buttons are pressed send RodEvent objects to
    listeners that have been previously setup.

    """

    def __init__(self):
        """Constructor"""
        super().__init__(self, "BUTTON")
        self.active = False  # type: bool
        self.channels = set()  # type: Set
        """ a set of button integers for the buttons actively being listened to """
        if GPIO.getmode() is None:
            GPIO.setmode(GPIO.BOARD)  # Default to physical pin numbering if not set
        self.valid_channels = self.get_valid_channels()  # type: list[int]
        """ a list of valid button integers that can be listened to based on the current GPIO mode """

    @classmethod
    def get_valid_channels(cls) -> list[int]:
        """ get the valid channels for testing based on the current GPIO mode """
        mode = GPIO.getmode()

        if mode == GPIO.BCM:
            # GPIOs exposed on the Raspberry Pi 4 header
            return [
                2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 25, 26, 27
            ]

        elif mode == GPIO.BOARD:
            # Physical pin numbers corresponding to GPIOs
            return [
                3, 5, 7, 8, 10, 11, 12, 13, 15, 16,
                18, 19, 21, 22, 23, 24, 26, 27, 28,
                29, 31, 32, 33, 35, 36, 37, 38, 40
            ]

        raise RuntimeError("GPIO mode not set or unsupported mode: {}".format(mode))


    def __hash__(self):
        """ Hash based on active state, channels, and listeners. Note that the order of channels and listeners does not affect the hash. """
        return hash((self.active, frozenset(self.channels), tuple(self.listeners)))

    def activate(self) -> None:
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        self.active = True

    def deactivate(self) -> None:
        for channel in set(self.channels):  # Create a copy to avoid modification during iteration
            self.channel_remove(channel)
        GPIO.cleanup()  # Clean up
        self.active = False

    def channel_add(self, channel: int) -> None:
        """add a button to those being listened to"""
        if not self.active:
            raise RuntimeError("ButtonEventGenerator not active")
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

    def _button_callback(self, channel: int) -> None:
        print(f"Button {channel} was pushed!")
        now = 0  # TODO
        event = RodEventButton(str(channel), now)
        for listener in self.listeners:
            listener.recieve_event(event)
