"""test"""

from __future__ import absolute_import
import unittest

from brain.rodeventbutton import RodEventButton


class TestRodEventButton(unittest.TestCase):
    """test"""

    def test_constructor(self):
        """test"""
        event = RodEventButton("TEST_01")
        self.assertTrue(isinstance(event, RodEventButton))


if __name__ == "__main__":
    unittest.main()
