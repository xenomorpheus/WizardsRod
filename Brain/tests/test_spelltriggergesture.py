""" test """
from __future__ import absolute_import
import unittest

from spelltriggergesture import SpellTriggerGesture


class TestSpellTriggerGesture(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        stg = SpellTriggerGesture('gesture')
        self.assertTrue(isinstance(stg, SpellTriggerGesture))

    # Only the gesture matters, not the name
    def test_match_trigger(self):
        """ test """
        stg1 = SpellTriggerGesture('gesture1')
        stg2 = SpellTriggerGesture('gesture1')
        stg3 = SpellTriggerGesture('gesture2')
        self.assertEqual(stg1, stg2)
        self.assertNotEqual(stg1, stg3)


if __name__ == '__main__':
    unittest.main()
