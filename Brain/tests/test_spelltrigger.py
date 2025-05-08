""" test """
from __future__ import absolute_import
import unittest

from time import gmtime
from spelltriggertype import SpellTriggerType
from staffevent import StaffEvent


class TestSpellTriggerType(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        spell_trigger = SpellTriggerType('Abracadabra')
        self.assertTrue(isinstance(spell_trigger, SpellTriggerType))

    def test_get_name(self):
        """ test """
        spell_trigger = SpellTriggerType('Abracadabra')
        self.assertEqual('Abracadabra', spell_trigger.get_name())

    def test_equal(self):
        """ test """
        spell_trigger1 = SpellTriggerType('Abracadabra')
        spell_trigger2 = SpellTriggerType('Abracadabra')
        spell_trigger3 = SpellTriggerType('Abracadabra2')
        self.assertEqual(spell_trigger1, spell_trigger2)
        self.assertNotEqual(spell_trigger1, spell_trigger3)
        self.assertTrue(spell_trigger1.__eq__(spell_trigger2), "basic equals")

    def test_hash(self):
        """ test """
        spell_trigger1 = SpellTriggerType('Abracadabra')
        spell_trigger2 = SpellTriggerType('Abracadabra')
        spell_trigger3 = SpellTriggerType('Abracadabra2')
        self.assertEqual(spell_trigger1.__hash__(),
                         spell_trigger2.__hash__(), 'hash spell_trigger1 and spell_trigger2')
        self.assertNotEqual(spell_trigger1.__hash__(),
                            spell_trigger3.__hash__(), 'hash spell_trigger1 and spell_trigger3')

    def test_is_triggerd_by(self):
        """ test """
        spell_trigger = SpellTriggerType('Button1')
        staff_event = StaffEvent(spell_trigger.get_name(), gmtime())
        self.assertTrue(spell_trigger.is_triggerd_by(staff_event))


if __name__ == '__main__':
    unittest.main()
