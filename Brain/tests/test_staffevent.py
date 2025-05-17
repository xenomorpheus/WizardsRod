"""test"""

from __future__ import absolute_import
import unittest

from brain.staffevent import StaffEvent


class TestStaffEvent(unittest.TestCase):
    """test"""

    def test_constructor(self):
        """test"""
        event = StaffEvent("TEST_01", 0)
        self.assertTrue(isinstance(event, StaffEvent))

    def test_constructor_with_type(self):
        """test"""
        event = StaffEvent("TEST_01", 0, "sometype")
        self.assertEqual("sometype", event.get_staffevent_type())

    def test_get_name(self):
        """test"""
        event = StaffEvent("TEST_01", 0)
        self.assertEqual("TEST_01", event.get_name())

    def test_get_created(self):
        """test"""
        event = StaffEvent("TEST_01", 99)
        self.assertEqual(99, event.get_created())

    def test_get_staffevent_type(self):
        """test"""
        event = StaffEvent("TEST_01", 0)
        self.assertEqual("none", event.get_staffevent_type())

    def test_equal(self):
        """test"""
        staff_event1 = StaffEvent("TEST_01", 4)
        staff_event2 = StaffEvent("TEST_01", 4)
        staff_event3 = StaffEvent("TEST_02", 4)
        self.assertEqual(staff_event1, staff_event2)
        self.assertNotEqual(staff_event1, staff_event3)
        self.assertNotEqual(staff_event1, 1)

    def test_hash(self):
        """test"""
        staff_event1 = StaffEvent("TEST_01", 4)
        staff_event2 = StaffEvent("TEST_01", 4)
        staff_event3 = StaffEvent("TEST_02", 4)
        self.assertEqual(hash(staff_event1), hash(staff_event2), "hash staff_event1 and staff_event2")
        self.assertNotEqual(hash(staff_event1), hash(staff_event3), "hash staff_event1 and staff_event3")


if __name__ == "__main__":
    unittest.main()
