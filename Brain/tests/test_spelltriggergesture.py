import unittest

from spelltriggergesture import SpellTriggerGesture
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


if __name__ == '__main__':
    unittest.main()
