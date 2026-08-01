"""test"""

from __future__ import absolute_import
import unittest
from unittest.mock import Mock

from brain.buttoneventgenerator import ButtonEventGenerator

# from brain.const import ST_GESTURE


class TestButtonEventGenerator(unittest.TestCase):
    """test"""

    @classmethod
    def setUpClass(cls):
        """test"""

    def setUp(self):
        self.mock_gpio = Mock()
        self.mock_gpio.BOARD = 10
        self.mock_gpio.IN = 1
        self.mock_gpio.PUD_DOWN = 2
        self.mock_gpio.RISING = 3

        self.mock_gpio.getmode.return_value = self.mock_gpio.BOARD

    def test_constructor(self):
        generator = ButtonEventGenerator(self.mock_gpio)
        self.assertIsInstance(generator, ButtonEventGenerator)

    def test_hash(self):
        """test"""
        generator1 = ButtonEventGenerator(self.mock_gpio)
        generator2 = ButtonEventGenerator(self.mock_gpio)
        self.assertEqual(hash(generator1), hash(generator2))

    def test_activate_deactivate(self):
        """test"""
        generator = ButtonEventGenerator(self.mock_gpio)
        generator.activate()
        self.assertTrue(generator.active)
        generator.deactivate()
        self.assertFalse(generator.active)

    def test_deactivate_clears_channels(self):
        """test"""
        generator = ButtonEventGenerator(self.mock_gpio)
        generator.activate()
        channel = generator.get_valid_channels()[0]
        generator.add_channel(channel)
        self.assertIn(channel, generator.channels)
        generator.deactivate()
        self.assertNotIn(channel, generator.channels)

    def test_activate_add_channel_throws(self):
        """test"""
        generator = ButtonEventGenerator(self.mock_gpio)
        channel = generator.get_valid_channels()[0]
        with self.assertRaises(RuntimeError):
            generator.add_channel(channel)

    def test_add_and_remove_channel(self):
        """test"""
        generator = ButtonEventGenerator(self.mock_gpio)
        generator.activate()
        channel = generator.get_valid_channels()[0]
        generator.add_channel(channel)
        self.assertIn(channel, generator.channels)
        generator.channel_remove(channel)
        self.assertNotIn(channel, generator.channels)
