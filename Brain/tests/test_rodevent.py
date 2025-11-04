"""test"""

from __future__ import absolute_import
import unittest

from brain.rodevent import RodEvent


class TestRodEvent(unittest.TestCase):
    """test"""

    def test_constructor(self):
        """test"""
        event = RodEvent("TEST_01", 0)
        self.assertTrue(isinstance(event, RodEvent))

    def test_constructor_with_type(self):
        """test"""
        event = RodEvent("TEST_01", 0, "sometype")
        self.assertEqual("sometype", event.get_event_type())

    def test_get_name(self):
        """test"""
        event = RodEvent("TEST_01", 0)
        self.assertEqual("TEST_01", event.get_name())

    def test_get_created(self):
        """test"""
        event = RodEvent("TEST_01", 99)
        self.assertEqual(99, event.get_created())

    def test_get_event_type(self):
        """test"""
        event = RodEvent("TEST_01", 0)
        self.assertEqual("none", event.get_event_type())

    def test_equal(self):
        """test"""
        rod_event1 = RodEvent("TEST_01", 4)
        rod_event2 = RodEvent("TEST_01", 4)
        rod_event3 = RodEvent("TEST_02", 4)
        self.assertEqual(rod_event1, rod_event2)
        self.assertNotEqual(rod_event1, rod_event3)
        self.assertNotEqual(rod_event1, 1)

    def test_hash(self):
        """test"""
        rod_event1 = RodEvent("TEST_01", 4)
        rod_event2 = RodEvent("TEST_01", 4)
        rod_event3 = RodEvent("TEST_02", 4)
        self.assertEqual(hash(rod_event1), hash(rod_event2), "hash rod_event1 and rod_event2")
        self.assertNotEqual(hash(rod_event1), hash(rod_event3), "hash rod_event1 and rod_event3")


if __name__ == "__main__":
    unittest.main()
