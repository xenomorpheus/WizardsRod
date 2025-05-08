import unittest
from time import gmtime

from spelltriggergesture import SpellTriggerGesture
from staffevent import StaffEvent
from const.staffeventconst import StaffEventConst as event


class TestSpellTriggerGesture(unittest.TestCase):

    def test_constructor(self):
        st = SpellTriggerGesture('Abracadabra')

    # Only the gesture matters, not the name
    def test_matchTrigger(self):
        st1 = SpellTriggerGesture('Abracadabra1')
        st2 = SpellTriggerGesture('Abracadabra1')
        st3 = SpellTriggerGesture('Abracadabra2')
        self.assertEqual(st1, st2)
        self.assertNotEqual(st1, st3)


    def test_isTriggerdBy(self):
        name = 'Button1'
        st = SpellTriggerGesture(name)
        se = StaffEvent(name, gmtime())
        self.assertTrue(st.isTriggerdBy(se))

if __name__ == '__main__':
    unittest.main()
