import unittest

from spelltrigger import SpellTrigger

class TestSpellTrigger(unittest.TestCase):

    def test_constructor(self):
        st = SpellTrigger('Abracadabra')

    def test_getName(self):
        st = SpellTrigger('Abracadabra')
        self.assertEqual('Abracadabra', st.getName())

    def test_equal(self):
        st1 = SpellTrigger('Abracadabra')
        st2 = SpellTrigger('Abracadabra')
        st3 = SpellTrigger('Abracadabra2')
        self.assertEqual(st1, st2)
        self.assertNotEqual(st1, st3)


if __name__ == '__main__':
    unittest.main()
