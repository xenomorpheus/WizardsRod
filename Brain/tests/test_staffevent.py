import unittest

from staffevent import StaffEvent
from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture


class TestStaffEvent(unittest.TestCase):

    def test_constructor(self):
        st = StaffEvent("Test Event 01", gesture.Test01, 0)

    def test_getName(self):
        st = StaffEvent("Test Event 01", gesture.Test01, 0)
        self.assertEqual("Test Event 01", st.getName())

    def test_getTrigger(self):
        st = StaffEvent("Test Event 01", gesture.Test01, 99)
        self.assertEqual(gesture.Test01, st.getTrigger())

    def test_getCreated(self):
        st = StaffEvent("Test Event 01", gesture.Test01, 99)
        self.assertEqual(99, st.getCreated())

    def test_equal(self):
        st1 = StaffEvent("Test Event 01", gesture.Test01, 4)
        st2 = StaffEvent("Test Event 01", gesture.Test01, 4)
        st3 = StaffEvent("Test Event 02", gesture.Test01, 4)
        st4 = StaffEvent("Test Event 01", gesture.Test02, 4)
        self.assertEqual(st1, st2)
        self.assertNotEqual(st1, st3)
        self.assertNotEqual(st1, st4)


if __name__ == '__main__':
    unittest.main()
