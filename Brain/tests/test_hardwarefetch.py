"""test"""

from __future__ import absolute_import
import unittest

from brain.hardwarefetch import HardwareFetch


class TestHardwareFetch(unittest.TestCase):
    """test"""

    def test_constructor(self):
        """test"""
        hwf = HardwareFetch()
        self.assertTrue(isinstance(hwf, HardwareFetch))

    def test_get(self):
        """test"""
        hwf = HardwareFetch()
        hw = hwf.get("BUTTON")
        self.assertEqual("BUTTON", hw.get_hardware_type())

    def test_get_invalid(self):
        """test"""
        hwf = HardwareFetch()
        with self.assertRaises(IOError):
            hwf.get("INVALID")

    def test_str(self):
        """test"""
        hwf = HardwareFetch()
        self.assertEqual("HardwareFetch", str(hwf))


if __name__ == "__main__":
    unittest.main()
