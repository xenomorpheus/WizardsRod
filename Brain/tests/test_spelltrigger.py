from __future__ import absolute_import
import unittest

from spelltrigger import SpellTrigger
from staffevent import StaffEvent
from time import gmtime

class TestSpellTrigger(unittest.TestCase):

    def test_constructor(self):
        spell_trigger = SpellTrigger('Abracadabra')
        self.assertTrue( isinstance(spell_trigger, SpellTrigger) )

    def test_get_name(self):
        spell_trigger = SpellTrigger('Abracadabra')
        self.assertEqual('Abracadabra', spell_trigger.get_name())

    def test_equal(self):
        spell_trigger1 = SpellTrigger('Abracadabra')
        spell_trigger2 = SpellTrigger('Abracadabra')
        spell_trigger3 = SpellTrigger('Abracadabra2')
        self.assertEqual(spell_trigger1, spell_trigger2)
        self.assertNotEqual(spell_trigger1, spell_trigger3)
        self.assertTrue(spell_trigger1.__eq__(spell_trigger2), "basic equals")

    def test_hash(self):
        spell_trigger1 = SpellTrigger('Abracadabra')
        spell_trigger2 = SpellTrigger('Abracadabra')
        spell_trigger3 = SpellTrigger('Abracadabra2')
        self.assertEqual(spell_trigger1.__hash__(), spell_trigger2.__hash__(), 'hash spell_trigger1 and spell_trigger2')
        self.assertNotEqual(spell_trigger1.__hash__(), spell_trigger3.__hash__(), 'hash spell_trigger1 and spell_trigger3')

    def test_is_triggerd_by(self):
        spell_trigger = SpellTrigger('Button1')
        staff_event = StaffEvent(spell_trigger.get_name(), gmtime())
        self.assertTrue(spell_trigger.is_triggerd_by(staff_event))

if __name__ == '__main__':
    unittest.main()
