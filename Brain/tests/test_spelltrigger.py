""" test """
from __future__ import absolute_import
import unittest

from time import gmtime
from spelltrigger import SpellTrigger
from staffevent import StaffEvent
import tests


class TestSpellTrigger(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        spell_trigger = SpellTrigger(tests.SPELL_TRIGGER_TYPE['TEST_01'])
        self.assertTrue(isinstance(spell_trigger, SpellTrigger))

    def test_get_name(self):
        """ test """
        spell_trigger = SpellTrigger('test trigger')
        self.assertEqual('test trigger', spell_trigger.
                         get_name())

    def test_get_name_with_type(self):
        """ test """
        spell_trigger_type = tests.SPELL_TRIGGER_TYPE['TEST_01']
        spell_trigger = SpellTrigger('test trigger', spell_trigger_type)
        self.assertEqual('test trigger', spell_trigger.
                         get_name())

    def test_get_type(self):
        """ test """
        spell_trigger_type = tests.SPELL_TRIGGER_TYPE['TEST_01']
        spell_trigger = SpellTrigger('my trigger', spell_trigger_type)
        self.assertEqual(spell_trigger_type, spell_trigger.get_type())

    def test_equal(self):
        """ test """
        spell_trigger1 = SpellTrigger('trigger 01',
                                      tests.SPELL_TRIGGER_TYPE['TEST_01'])
        spell_trigger2 = SpellTrigger('trigger 01',
                                      tests.SPELL_TRIGGER_TYPE['TEST_01'])
        spell_trigger3 = SpellTrigger('trigger 02',
                                      tests.SPELL_TRIGGER_TYPE['TEST_02'])
        self.assertEqual(spell_trigger1, spell_trigger2)
        self.assertNotEqual(spell_trigger1, spell_trigger3)
        self.assertTrue(spell_trigger1.__eq__(spell_trigger2), "basic equals")

    def test_hash(self):
        """ test """
        spell_trigger1 = SpellTrigger('trigger 01',
                                      tests.SPELL_TRIGGER_TYPE['TEST_01'])
        spell_trigger2 = SpellTrigger('trigger 01',
                                      tests.SPELL_TRIGGER_TYPE['TEST_01'])
        spell_trigger3 = SpellTrigger('trigger 02',
                                      tests.SPELL_TRIGGER_TYPE['TEST_02'])
        self.assertEqual(spell_trigger1.__hash__(),
                         spell_trigger2.__hash__(),
                         'hash spell_trigger1 and spell_trigger2')
        self.assertNotEqual(spell_trigger1.__hash__(),
                            spell_trigger3.__hash__(),
                            'hash spell_trigger1 and spell_trigger3')

    def test_is_triggerd_by(self):
        """ test """
        spell_trigger = SpellTrigger('TEST_01')
        staff_event = StaffEvent('TEST_01', gmtime())
        self.assertTrue(spell_trigger.is_triggerd_by(staff_event))

    def test_is_triggerd_by_with_type(self):
        """ test """
        spell_trigger = SpellTrigger('TEST_01', type='foo')
        staff_event = StaffEvent('TEST_01', gmtime(), type='foo')
        self.assertTrue(spell_trigger.is_triggerd_by(staff_event))

    def test_is_triggerd_by_with_wrong_type(self):
        """ test """
        spell_trigger = SpellTrigger('TEST_01', type='foo')
        staff_event = StaffEvent('TEST_01', gmtime(), type='wrong')
        self.assertFalse(spell_trigger.is_triggerd_by(staff_event))


if __name__ == '__main__':
    unittest.main()
