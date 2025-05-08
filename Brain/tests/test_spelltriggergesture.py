import unittest

from spelltriggergesture import SpellTriggerGesture


class TestSpellTriggerGesture(unittest.TestCase):

    def test_constructor(self):
        st = SpellTriggerGesture('Abracadabra', 123)

    def test_getGesture(self):
        st = SpellTriggerGesture('Abracadabra', 123)
        self.assertEqual(123, st.getGesture())

    # Only the gesture matters, not the name
    def test_matchTrigger(self):
        st1 = SpellTriggerGesture('Abracadabra1', 123)
        st2 = SpellTriggerGesture('Abracadabra2', 123)
        st3 = SpellTriggerGesture('Abracadabra3', 456)
        self.assertTrue(st1.matchTrigger(st2))
        self.assertFalse(st1.matchTrigger(st3))


if __name__ == '__main__':
    unittest.main()
