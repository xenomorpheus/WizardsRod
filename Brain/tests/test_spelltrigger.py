import unittest

from spelltrigger import SpellTrigger
from staffevent import StaffEvent
from time import gmtime

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

    def test_isTriggerdBy(self):
        st = SpellTrigger('Button1')
        se = StaffEvent(st.getName(), st, gmtime())
        self.assertTrue(st.isTriggerdBy(se))

if __name__ == '__main__':
    unittest.main()
