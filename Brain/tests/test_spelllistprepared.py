import unittest

import spelllistprepared

class TestSpellTrigger(unittest.TestCase):

    def test_constructor(self):
        st = Spell('Fire Ball')

    def test_getName(self):
        st = Spell('Fire Ball')
        self.assertEqual('Fire Ball', st.getName())

    def test_equal(self):
        st1 = Spell('Fire Ball')
        st2 = Spell('Fire Ball, Lessor')
        st3 = Spell('Fire Ball, Greater')
        self.assertEqual(st1, st2)
        self.assertNotEqual(st1, st3)


if __name__ == '__main__':
    unittest.main()