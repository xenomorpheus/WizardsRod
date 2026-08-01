"""
ButtonEventGenerator
"""

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

    def __init__(self, gpio=None):
        """Constructor"""
        super().__init__("BUTTON")
        self.gpio = gpio or GPIO
        self.active: bool = False
        self.channels: set[int] = set()
        """ a set of button integers for the buttons actively being listened to """
        if self.gpio.getmode() is None:
            self.gpio.setmode(self.gpio.BOARD)  # Default to physical pin numbering if not set
        self.valid_channels: list[int] = self.get_valid_channels()
        """ a list of valid button integers that can be listened to based on the current GPIO mode """

    def get_valid_channels(self) -> list[int]:
        """get the valid channels for testing based on the current GPIO mode"""
        mode = self.gpio.getmode()

        if mode == self.gpio.BCM:
            # GPIOs exposed on the Raspberry Pi 4 header
            return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

        if mode == self.gpio.BOARD:
            # Physical pin numbers corresponding to GPIOs
            return [
                3,
                5,
                7,
                8,
                10,
                11,
                12,
                13,
                15,
                16,
                18,
                19,
                21,
                22,
                23,
                24,
                26,
                27,
                28,
                29,
                31,
                32,
                33,
                35,
                36,
                37,
                38,
                40,
            ]

        raise RuntimeError(f"GPIO mode not set or unsupported mode: {mode}")

    def __hash__(self):
        """Hash based on active state, channels, and listeners."""
        return hash((self.active, frozenset(self.channels), tuple(self.listeners)))

    def activate(self) -> None:
        self.gpio.setwarnings(False)  # Ignore warning for now
        self.gpio.setmode(self.gpio.BOARD)  # Use physical pin numbering
        self.active = True

    def deactivate(self) -> None:
        for channel in set(self.channels):  # Create a copy to avoid modification during iteration
            self.channel_remove(channel)
        self.gpio.cleanup()  # Clean up
        self.active = False

    def add_channel(self, channel: int) -> None:
        """add a button to those being listened to"""

        if not self.active:
            raise RuntimeError("ButtonEventGenerator not active")
        # Set pin channel to be an input pin and set initial value to be
        # pulled low (off).
        # Setup event on pin channel rising edge. Ignore further edges for
        # 200ms for switch bounce handling.
        # Multiple callback handlers can be added
        self.gpio.add_event_detect(channel, self.gpio.RISING, callback=self._button_callback, bouncetime=200)
        self.channels.add(channel)

    def channel_remove(self, channel: int) -> None:
        """remove a button from those being listened to"""
        self.gpio.remove_event_detect(channel)
        self.channels.remove(channel)

    def _button_callback(self, channel: int) -> None:
        print(f"Button {channel} was pushed!")
        now = 0  # TODO
        event = RodEventButton(str(channel), now)
        for listener in self.listeners:
            listener.recieve_event(event)
