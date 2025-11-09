"""test"""

from __future__ import absolute_import
import unittest

from brain.hardwarefetch import HardwareFetch
from brain.hardware import Hardware


class FakeHardware(Hardware):
    """
    Send RodEvent objects to listeners that have been previously setup.
    """

    def __init__(self):
        """Constructor"""
        super().__init__(self, "none")


class TestHardwareFetch(unittest.TestCase):
    """test"""

    def test_constructor(self):
        """test"""
        hwf = HardwareFetch()
        self.assertTrue(isinstance(hwf, HardwareFetch))

    def test_get_invalid(self):
        """test"""
        hwf = HardwareFetch()
        with self.assertRaises(IOError):
            hwf.get("INVALID")

    def test_set_and_get(self):
        """test"""
        hwf = HardwareFetch()
        fake_hw = FakeHardware()
        hwf.set(fake_hw.get_hardware_type(), fake_hw)
        self.assertEqual(fake_hw, hwf.get(fake_hw.get_hardware_type()))
