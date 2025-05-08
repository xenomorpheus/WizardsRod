from __future__ import absolute_import
import unittest

#from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture
#from const.spellhardwareconst import SpellHardwareConst as hw
#from spell import Spell
from staff import Staff


class TestStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.name = "Test Staff"

    def test_constructor(self):
        st = Staff(name=self.name)
        self.assertTrue( isinstance(st, Staff) )

    def test_getName(self):
        st = Staff(name=self.name)
        self.assertEqual(self.name, st.getName())

if __name__ == '__main__':
    unittest.main()
