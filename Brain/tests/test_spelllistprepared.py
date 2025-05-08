""" test """

from __future__ import absolute_import
import unittest

from spelllistprepared import SpellListPrepared
from spell import Spell
from spelltrigger import SpellTrigger
from staff import Staff
from staffevent import StaffEvent
import const


class TestSpellListPrepared(unittest.TestCase):
    """ test """


    def setUp(self):
        """ setup all tests """
        self.perform_action_calls = set()

    def perform_action(self, spell, staff):
        """ detect if this method was called.
        simulate the spell performing actions. """
        self.perform_action_calls.add(staff.name+"="+spell.name)

    def test_constructor(self):
        """ test """
        slp = SpellListPrepared(None)
        self.assertFalse(slp is None, 'must not be None')

    def test_spell_add(self):
        """ test """
        test_spell01 = Spell('Test Spell 01')
        slp = SpellListPrepared(None)
        slp_got = slp.spell_add(test_spell01)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spell_add_list(self):
        """ test """
        test_spell01 = Spell('Test Spell 01')
        slp = SpellListPrepared(None)
        slp_got = slp.spell_add_list([test_spell01])
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spell_del(self):
        """ test """
        test_spell01 = Spell('Test Spell 01')
        slp = SpellListPrepared(None)
        slp_got = slp.spell_del(test_spell01)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_receive_events_no_spells_no_events(self):
        """ test """
        slp = SpellListPrepared(None)
        new_events = []
        slp.receive_events(new_events)

    def test_receive_events_no_spells_some_events(self):
        """ test """
        slp = SpellListPrepared(None)
        new_events = [const.EVENT["TEST_01"], const.EVENT["TEST_02"]]
        slp.receive_events(new_events)

    # Only accept events that are for our prepared spells
    def test_receive_events_some_spells_unwanted_events(self):
        """ test """
        triggers = [
            SpellTrigger('TEST_01'),
            SpellTrigger('TEST_02')]
        test_spell01 = Spell("Test Spell 01").set_trigger_sequence(triggers)
        test_spell01.set_perform_actions(self.perform_action)
        slp = SpellListPrepared(None).spell_add(test_spell01)
        new_events = [
            StaffEvent('Event 03', 4)]
        slp.receive_events(new_events)
        self.assertFalse(self.perform_action_calls)

    def test_receive_events_one_spells_no_events(self):
        """ test """
        test_spell01 = Spell('Test Spell 01')
        test_spell01.set_perform_actions(self.perform_action)
        slp = SpellListPrepared(None).spell_add(test_spell01)
        new_events = []
        slp.receive_events(new_events)
        self.assertFalse(self.perform_action_calls)

    def test_receive_events_some_spells(self):
        """ test """
        triggers = [
            SpellTrigger('TEST_01'),
            SpellTrigger('TEST_02')]
        test_spell01 = Spell("test_receives_event_some_spells")
        test_spell01.set_trigger_sequence(triggers)
        test_spell01.set_perform_actions(self.perform_action)
        staff = Staff("The Staff")
        slp = SpellListPrepared(staff).spell_add(test_spell01)
        # Gesture Test03 will be ignored
        events = [
            StaffEvent('TEST_01', 4),
            StaffEvent('TEST_02', 4),
            StaffEvent('TEST_03', 4)]
        slp.receive_events(events)
        self.assertEqual(set([staff.name+"="+test_spell01.name]),
                         self.perform_action_calls)

    def test_get_hardware_hints(self):
        """ test """
        test_spell01 = Spell("Test Spell 01").set_hardware_set(['Button01'])
        test_spell02 = Spell("Test Spell 02").set_hardware_set(['Button02',
                                                                'Button03'])
        slp = SpellListPrepared(None).spell_add_list([test_spell01,
                                                      test_spell02])
        hwl = slp.get_hardware_hints()
        self.assertEqual(set(['Button01', 'Button02', 'Button03']), set(hwl))


if __name__ == '__main__':
    unittest.main()
