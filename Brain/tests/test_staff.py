from __future__ import absolute_import
import unittest

# from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture
# from const.spellhardwareconst import SpellHardwareConst as hw
# from spell import Spell
from staff import Staff


class TestStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.name = "Test Staff"

    def test_constructor(self):
        staff = Staff(name=self.name)
        self.assertTrue(isinstance(staff, Staff))

    def test_get_name(self):
        staff = Staff(name=self.name)
        self.assertEqual(self.name, staff.get_name())


if __name__ == '__main__':
    unittest.main()
