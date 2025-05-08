import unittest

from staffevent import StaffEvent
from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture


class TestStaffEvent(unittest.TestCase):

    def test_constructor(self):
        st = StaffEvent("Test Event 01", 0)

    def test_getName(self):
        st = StaffEvent("Test Event 01", 0)
        self.assertEqual("Test Event 01", st.getName())

    def test_getCreated(self):
        st = StaffEvent("Test Event 01", 99)
        self.assertEqual(99, st.getCreated())

    def test_equal(self):
        st1 = StaffEvent("Test Event 01", 4)
        st2 = StaffEvent("Test Event 01", 4)
        st3 = StaffEvent("Test Event 02", 4)
        self.assertTrue(st1.__eq__(st2))
        self.assertEqual(st1, st2)
        self.assertNotEqual(st1, st3)

    def test_hash(self):
        st1 = StaffEvent("Test Event 01", 4)
        st2 = StaffEvent("Test Event 01", 4)
        st3 = StaffEvent("Test Event 02", 4)
        self.assertEqual(st1.__hash__(), st2.__hash__(), 'hash st1 and st2')
        self.assertNotEqual(st1.__hash__(), st3.__hash__(), 'hash st1 and st3')

if __name__ == '__main__':
    unittest.main()
