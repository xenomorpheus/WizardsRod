""" test """
from __future__ import absolute_import
import unittest
from time import gmtime

from spelltriggergesture import SpellTriggerGesture
from staffevent import StaffEvent


class TestSpellTriggerGesture(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        stg = SpellTriggerGesture('Abracadabra')
        self.assertTrue(isinstance(stg, SpellTriggerGesture))

    # Only the gesture matters, not the name
    def test_match_trigger(self):
        """ test """
        stg1 = SpellTriggerGesture('Abracadabra1')
        stg2 = SpellTriggerGesture('Abracadabra1')
        stg3 = SpellTriggerGesture('Abracadabra2')
        self.assertEqual(stg1, stg2)
        self.assertNotEqual(stg1, stg3)

    def test_is_triggerd_by(self):
        """ test """
        name = 'Button1'
        stg = SpellTriggerGesture(name)
        staff_event = StaffEvent(name, gmtime())
        self.assertTrue(stg.is_triggerd_by(staff_event))


if __name__ == '__main__':
    unittest.main()
