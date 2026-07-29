"""test"""

from __future__ import absolute_import
import unittest

from brain.buttoneventgenerator import ButtonEventGenerator

# from brain.const import ST_GESTURE


class TestButtonEventGenerator(unittest.TestCase):
    """test"""

    @classmethod
    def setUpClass(cls):
        """test"""

    def test_constructor(self):
        """test"""
        generator = ButtonEventGenerator()
        self.assertTrue(isinstance(generator, ButtonEventGenerator))

    def test_hash(self):
        """test"""
        generator1 = ButtonEventGenerator()
        generator2 = ButtonEventGenerator()
        self.assertEqual(hash(generator1), hash(generator2))

    def test_activate_deactivate(self):
        """test"""
        generator = ButtonEventGenerator()
        generator.activate()
        self.assertTrue(generator.active)
        generator.deactivate()
        self.assertFalse(generator.active)

    def test_deactivate_clears_channels(self):
        """test"""
        generator = ButtonEventGenerator()
        generator.activate()
        channel = generator.get_valid_channels()[0]
        generator.add_channel(channel)
        self.assertIn(channel, generator.channels)
        generator.deactivate()
        self.assertNotIn(channel, generator.channels)

    def test_activate_add_channel_throws(self):
        """test"""
        generator = ButtonEventGenerator()
        channel = generator.get_valid_channels()[0]
        with self.assertRaises(RuntimeError):
            generator.add_channel(channel)

    def test_add_and_remove_channel(self):
        """test"""
        generator = ButtonEventGenerator()
        generator.activate()
        channel = generator.get_valid_channels()[0]
        generator.add_channel(channel)
        self.assertIn(channel, generator.channels)
        generator.channel_remove(channel)
        self.assertNotIn(channel, generator.channels)
