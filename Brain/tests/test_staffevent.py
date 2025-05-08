from __future__ import absolute_import
import unittest

from staffevent import StaffEvent


class TestStaffEvent(unittest.TestCase):

    def test_constructor(self):
        staff_event = StaffEvent("Test Event 01", 0)
        self.assertTrue(isinstance(staff_event, StaffEvent))

    def test_get_name(self):
        staff_event = StaffEvent("Test Event 01", 0)
        self.assertEqual("Test Event 01", staff_event.get_name())

    def test_get_created(self):
        staff_event = StaffEvent("Test Event 01", 99)
        self.assertEqual(99, staff_event.get_created())

    def test_equal(self):
        staff_event1 = StaffEvent("Test Event 01", 4)
        staff_event2 = StaffEvent("Test Event 01", 4)
        staff_event3 = StaffEvent("Test Event 02", 4)
        self.assertTrue(staff_event1.__eq__(staff_event2))
        self.assertEqual(staff_event1, staff_event2)
        self.assertNotEqual(staff_event1, staff_event3)

    def test_hash(self):
        staff_event1 = StaffEvent("Test Event 01", 4)
        staff_event2 = StaffEvent("Test Event 01", 4)
        staff_event3 = StaffEvent("Test Event 02", 4)
        self.assertEqual(staff_event1.__hash__(), staff_event2.__hash__(), 'hash staff_event1 and staff_event2')
        self.assertNotEqual(staff_event1.__hash__(), staff_event3.__hash__(), 'hash staff_event1 and staff_event3')


if __name__ == '__main__':
    unittest.main()
