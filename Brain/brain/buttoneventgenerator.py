"""ButtonEventGenerator: turn hardware button presses into RodEvents."""

from __future__ import annotations

import logging
import time
from enum import Enum

from gpiozero import Button
from gpiozero.pins import Factory

from brain.hardware import Hardware
from brain.rodeventbutton import RodEventButton

log = logging.getLogger(__name__)


class PinNumbering(Enum):
    BOARD = "BOARD"  # physical header pin numbers
    BCM = "GPIO"  # Broadcom GPIO numbers


class ButtonEventGenerator(Hardware):
    """Send a RodEventButton to every listener when a hardware button is pressed."""

    BOUNCE_TIME = 0.2  # seconds

    VALID_CHANNELS: dict[PinNumbering, frozenset[int]] = {
        # GPIO2/3 (BOARD 3/5) are left out: their fixed I2C pull-ups
        # stop pulled-low buttons from working.
        PinNumbering.BCM: frozenset(range(4, 28)),
        PinNumbering.BOARD: frozenset(
            {
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
            }
        ),
    }

    def __init__(
        self,
        numbering: PinNumbering = PinNumbering.BOARD,
        pin_factory: Factory | None = None,
    ) -> None:
        super().__init__("BUTTON")
        self.numbering = numbering
        self._pin_factory = pin_factory  # None = gpiozero's default (lgpio on a Pi)
        self._buttons: dict[int, Button] = {}
        self.active = False

    @property
    def valid_channels(self) -> frozenset[int]:
        """Channels that can be listened to under the current numbering scheme."""
        return self.VALID_CHANNELS[self.numbering]

    @property
    def channels(self) -> set[int]:
        """Channels currently being listened to."""
        return set(self._buttons)

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        for channel in list(self._buttons):
            self.remove_channel(channel)
        self.active = False

    def add_channel(self, channel: int) -> None:
        """Start listening to a button."""
        if not self.active:
            raise RuntimeError("ButtonEventGenerator not active")
        if channel not in self.valid_channels:
            raise ValueError(f"{channel} is not a valid {self.numbering.name} channel")
        if channel in self._buttons:
            return
        button = Button(
            f"{self.numbering.value}{channel}",  # e.g. "BOARD11" or "GPIO17"
            pull_up=False,  # pulled low, press = rising edge
            bounce_time=self.BOUNCE_TIME,
            pin_factory=self._pin_factory,
        )
        button.when_pressed = lambda: self._on_press(channel)
        self._buttons[channel] = button

    def remove_channel(self, channel: int) -> None:
        """Stop listening to a button and release its pin."""
        if button := self._buttons.pop(channel, None):
            button.close()

    def _on_press(self, channel: int) -> None:
        log.info("Button %s pressed", channel)
        event = RodEventButton(str(channel), time.monotonic())
        for listener in self.listeners:
            listener.receive_event(event)
