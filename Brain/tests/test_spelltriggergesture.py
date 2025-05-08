""" test """
from __future__ import absolute_import
import unittest

from spelltriggertypegesture import SpellTriggerTypeGesture


class TestSpellTriggerTypeGesture(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        stg = SpellTriggerTypeGesture('gesture')
        self.assertTrue(isinstance(stg, SpellTriggerTypeGesture))

    # Only the gesture matters, not the name
    def test_match_trigger(self):
        """ test """
        stg1 = SpellTriggerTypeGesture('gesture1')
        stg2 = SpellTriggerTypeGesture('gesture1')
        stg3 = SpellTriggerTypeGesture('gesture2')
        self.assertEqual(stg1, stg2)
        self.assertNotEqual(stg1, stg3)


if __name__ == '__main__':
    unittest.main()
