"""Unit tests for ButtonEventGenerator, using gpiozero's mock pins."""

import unittest
from unittest.mock import ANY, Mock, patch

from gpiozero.pins.mock import MockFactory

from brain.buttoneventgenerator import ButtonEventGenerator, PinNumbering


class TestButtonEventGenerator(unittest.TestCase):
    """Tests for ButtonEventGenerator."""

    def setUp(self):
        self.factory = MockFactory()
        self.addCleanup(self.factory.close)

    def make_generator(self, numbering=PinNumbering.BOARD, active=True):
        """Create a generator on mock pins; deactivated automatically after the test."""
        generator = ButtonEventGenerator(numbering, pin_factory=self.factory)
        if active:
            generator.activate()
        self.addCleanup(generator.deactivate)
        return generator

    @staticmethod
    def press(generator, channel):
        """Simulate a button press on a channel."""
        generator._buttons[channel].pin.drive_high()

    # --- construction ---

    def test_constructor_defaults(self):
        """A new generator uses BOARD numbering, is inactive and has no channels."""
        generator = self.make_generator(active=False)
        self.assertEqual(generator.numbering, PinNumbering.BOARD)
        self.assertFalse(generator.active)
        self.assertEqual(generator.channels, set())

    def test_valid_channels_board(self):
        """BOARD numbering exposes the physical header pins, including 27 and 28."""
        generator = self.make_generator(PinNumbering.BOARD, active=False)
        self.assertEqual(len(generator.valid_channels), 26)
        self.assertIn(27, generator.valid_channels)
        self.assertNotIn(1, generator.valid_channels)  # 3.3V pin
        self.assertNotIn(3, generator.valid_channels)  # GPIO2, fixed pull-up

    def test_valid_channels_bcm(self):
        """BCM numbering exposes GPIO4 to GPIO27."""
        generator = self.make_generator(PinNumbering.BCM, active=False)
        self.assertEqual(generator.valid_channels, frozenset(range(4, 28)))

    # --- activation ---

    def test_activate_deactivate(self):
        """activate() and deactivate() toggle the active flag."""
        generator = self.make_generator(active=False)
        generator.activate()
        self.assertTrue(generator.active)
        generator.deactivate()
        self.assertFalse(generator.active)

    def test_add_channel_when_inactive_raises(self):
        """Adding a channel before activate() raises RuntimeError."""
        generator = self.make_generator(active=False)
        with self.assertRaises(RuntimeError):
            generator.add_channel(11)

    def test_deactivate_clears_channels(self):
        """deactivate() stops listening to every channel."""
        generator = self.make_generator()
        generator.add_channel(11)
        generator.add_channel(13)
        generator.deactivate()
        self.assertEqual(generator.channels, set())

    def test_deactivate_releases_pins(self):
        """Pins are released on deactivate(), so they can be claimed again."""
        generator = self.make_generator()
        generator.add_channel(11)
        generator.deactivate()
        generator.activate()
        generator.add_channel(11)  # raises GPIOPinInUse if the pin was not closed
        self.assertIn(11, generator.channels)

    # --- channels ---

    def test_add_and_remove_channel(self):
        """A channel can be added and then removed."""
        generator = self.make_generator()
        generator.add_channel(11)
        self.assertIn(11, generator.channels)
        generator.remove_channel(11)
        self.assertNotIn(11, generator.channels)

    def test_add_channel_twice_is_harmless(self):
        """Adding the same channel twice keeps a single listener on it."""
        generator = self.make_generator()
        generator.add_channel(11)
        generator.add_channel(11)
        self.assertEqual(generator.channels, {11})

    def test_remove_unknown_channel_is_harmless(self):
        """Removing a channel that was never added does nothing."""
        generator = self.make_generator()
        generator.remove_channel(11)
        self.assertEqual(generator.channels, set())

    def test_invalid_channel_raises(self):
        """Channels outside the valid set raise ValueError in both numbering schemes."""
        cases = [(PinNumbering.BOARD, 1), (PinNumbering.BOARD, 41), (PinNumbering.BCM, 1), (PinNumbering.BCM, 28)]
        for numbering, channel in cases:
            with self.subTest(numbering=numbering, channel=channel):
                generator = self.make_generator(numbering)
                with self.assertRaises(ValueError):
                    generator.add_channel(channel)

    def test_every_valid_channel_can_be_added(self):
        """gpiozero accepts every channel in both valid-channel lists."""
        for numbering in PinNumbering:
            with self.subTest(numbering=numbering):
                generator = self.make_generator(numbering)
                for channel in generator.valid_channels:
                    generator.add_channel(channel)
                self.assertEqual(generator.channels, set(generator.valid_channels))
                generator.deactivate()

    def test_numbering_maps_to_same_gpio(self):
        """BOARD 11 and BCM 17 refer to the same GPIO."""
        # Check: relies on gpiozero 2.x's pin.info.name.
        board = self.make_generator(PinNumbering.BOARD)
        board.add_channel(11)
        self.assertEqual(board._buttons[11].pin.info.name, "GPIO17")

    # --- events ---

    @patch("brain.buttoneventgenerator.RodEventButton")
    def test_press_sends_event_to_listeners(self, mock_event_cls):
        """A button press sends one RodEventButton to every listener."""
        generator = self.make_generator()
        listeners = [Mock(spec=["receive_event"]), Mock(spec=["receive_event"])]
        for listener in listeners:
            generator.listener_add(listener)
        generator.add_channel(11)

        self.press(generator, 11)

        mock_event_cls.assert_called_once_with("11", ANY)
        for listener in listeners:
            listener.receive_event.assert_called_once_with(mock_event_cls.return_value)

    def test_removed_channel_sends_no_events(self):
        """After remove_channel(), presses on the pin are ignored."""
        generator = self.make_generator()
        listener = Mock(spec=["receive_event"])
        generator.listener_add(listener)
        generator.add_channel(11)
        pin = generator._buttons[11].pin
        generator.remove_channel(11)

        pin.drive_high()

        listener.receive_event.assert_not_called()


if __name__ == "__main__":
    unittest.main()
