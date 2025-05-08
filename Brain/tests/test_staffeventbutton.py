""" test """
from __future__ import absolute_import
import unittest

from staffeventbutton import StaffEventButton


class TestStaffEventButton(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        event = StaffEventButton('TEST_01')
        self.assertTrue(isinstance(event, StaffEventButton))


if __name__ == '__main__':
    unittest.main()
