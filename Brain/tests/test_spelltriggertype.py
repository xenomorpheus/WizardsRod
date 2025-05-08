""" test """
from __future__ import absolute_import
import unittest

from spelltriggertype import SpellTriggerType


class TestSpellTriggerType(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        spell_trigger_type = SpellTriggerType('Abracadabra')
        self.assertTrue(isinstance(spell_trigger_type, SpellTriggerType))

    def test_get_name(self):
        """ test """
        spell_trigger_type = SpellTriggerType('Abracadabra')
        self.assertEqual('Abracadabra', spell_trigger_type.get_name())

    def test_equal(self):
        """ test """
        spell_trigger_type1 = SpellTriggerType('Abracadabra')
        spell_trigger_type2 = SpellTriggerType('Abracadabra')
        spell_trigger_type3 = SpellTriggerType('Abracadabra2')
        self.assertEqual(spell_trigger_type1, spell_trigger_type2)
        self.assertNotEqual(spell_trigger_type1, spell_trigger_type3)
        self.assertTrue(spell_trigger_type1.__eq__(spell_trigger_type2),
                        "basic equals")

    def test_hash(self):
        """ test """
        spell_trigger_type1 = SpellTriggerType('Abracadabra')
        spell_trigger_type2 = SpellTriggerType('Abracadabra')
        spell_trigger_type3 = SpellTriggerType('Abracadabra2')
        self.assertEqual(spell_trigger_type1.__hash__(),
                         spell_trigger_type2.__hash__(),
                         'hash spell_trigger1 and spell_trigger2')
        self.assertNotEqual(spell_trigger_type1.__hash__(),
                            spell_trigger_type3.__hash__(),
                            'hash spell_trigger1 and spell_trigger3')


if __name__ == '__main__':
    unittest.main()
