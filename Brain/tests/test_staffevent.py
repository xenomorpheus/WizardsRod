""" test """
from __future__ import absolute_import
import unittest

from staffevent import StaffEvent


class TestStaffEvent(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        staff_event = StaffEvent('TEST_01', 0)
        self.assertTrue(isinstance(staff_event, StaffEvent))

    def test_get_name(self):
        """ test """
        staff_event = StaffEvent('TEST_01', 0)
        self.assertEqual('TEST_01', staff_event.
                         get_name())

    def test_get_created(self):
        """ test """
        staff_event = StaffEvent('TEST_01', 99)
        self.assertEqual(99, staff_event.get_created())

    def test_get_event_type(self):
        """ test """
        staff_event = StaffEvent('TEST_01', 0)
        self.assertEqual('none', staff_event.
                         get_event_type())

    def test_equal(self):
        """ test """
        staff_event1 = StaffEvent('TEST_01', 4)
        staff_event2 = StaffEvent('TEST_01', 4)
        staff_event3 = StaffEvent('TEST_02', 4)
        self.assertTrue(staff_event1.__eq__(staff_event2))
        self.assertEqual(staff_event1, staff_event2)
        self.assertNotEqual(staff_event1, staff_event3)

    def test_hash(self):
        """ test """
        staff_event1 = StaffEvent('TEST_01', 4)
        staff_event2 = StaffEvent('TEST_01', 4)
        staff_event3 = StaffEvent('TEST_02', 4)
        self.assertEqual(staff_event1.__hash__(), staff_event2.__hash__(),
                         'hash staff_event1 and staff_event2')
        self.assertNotEqual(staff_event1.__hash__(), staff_event3.__hash__(),
                            'hash staff_event1 and staff_event3')


if __name__ == '__main__':
    unittest.main()
