""" test """

from __future__ import absolute_import
import unittest

from spelllistprepared import SpellListPrepared
from spell import Spell
from staffevent import StaffEvent
from const.spellbookmaster import SpellBookMaster
from const.spelltriggertypegestureconst import SpellTriggerTypeGestureConst as gesture
from const.staffeventconst import StaffEventConst as event


class TestSpellListPrepared(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ setup all tests """
        cls.spell = SpellBookMaster.TestSpell01

    def test_constructor(self):
        """ test """
        slp = SpellListPrepared(name='MyList')
        self.assertFalse(slp is None, 'must not be None')

    def test_get_name(self):
        """ test """
        slp = SpellListPrepared('MyList')
        self.assertEqual('MyList', slp.get_name())

    def test_spell_add(self):
        """ test """
        slp = SpellListPrepared('MyList')
        slp_got = slp.spell_add(self.spell)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spell_add_list(self):
        """ test """
        slp = SpellListPrepared('MyList')
        slp_got = slp.spell_add_list([self.spell])
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spell_del(self):
        """ test """
        slp = SpellListPrepared('MyList')
        slp_got = slp.spell_del(self.spell.name)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_accept_events_no_spells_no_events(self):
        """ test """
        slp = SpellListPrepared('MyList')
        new_events = []
        accepted_count = slp.accept_events(new_events)
        self.assertEqual(0, accepted_count)

    def test_accept_events_no_spells_some_events(self):
        """ test """
        slp = SpellListPrepared('MyList')
        new_events = [event.Test01, event.Test02]
        accepted_count = slp.accept_events(new_events)
        self.assertEqual(0, accepted_count)

    def test_accept_events_some_spells_some_events(self):
        """ test """
        triggers = [gesture.Test01, gesture.Test02]
        test_spell01 = Spell("Test Spell 01").set_trigger_sequence(triggers)
        slp = SpellListPrepared('MyList').spell_add(test_spell01)
        # Gesture Test03 will be ignored
        events = [
            StaffEvent(gesture.Test01.get_name(), 4),
            StaffEvent(gesture.Test02.get_name(), 4),
            StaffEvent(gesture.Test03.get_name(), 4)]
        accepted_count = slp.accept_events(events)
        self.assertEqual(2, accepted_count, 'accepted count')

    # Only accept events that are for our prepared spells
    def test_accept_events_some_spells_unwanted_events(self):
        """ test """
        triggers = [gesture.Test01, gesture.Test02]
        test_spell01 = Spell("Test Spell 01").set_trigger_sequence(triggers)
        slp = SpellListPrepared('MyList').spell_add(test_spell01)
        events = [
            StaffEvent("Event 03", 4)]
        accepted_count_got = slp.accept_events(events)
        self.assertEqual(0, accepted_count_got, 'accepted count')

    def test_get_triggered_spells_no_spells_no_events(self):
        """ test """
        slp = SpellListPrepared('MyList')
        new_events = []
        slp.accept_events(new_events)
        triggerd_spells = slp.get_triggered_spells()
        self.assertEqual([], triggerd_spells)

    def test_get_triggered_spells_one_spells_no_events(self):
        """ test """
        slp = SpellListPrepared('MyList').spell_add(self.spell)
        new_events = []
        slp.accept_events(new_events)
        triggerd_spells = slp.get_triggered_spells()
        self.assertEqual([], triggerd_spells, 'no triggered spells')

    def test_get_triggered_spells_some_spells(self):
        """ test """
        triggers = [gesture.Test01, gesture.Test02]
        test_spell01 = Spell("Test Spell 01").set_trigger_sequence(triggers)
        slp = SpellListPrepared('MyList').spell_add(test_spell01)
        # Gesture Test03 will be ignored
        events = [
            StaffEvent(gesture.Test01.get_name(), 4),
            StaffEvent(gesture.Test02.get_name(), 4),
            StaffEvent(gesture.Test03.get_name(), 4)]
        accepted_count = slp.accept_events(events)
        self.assertEqual(2, accepted_count, 'accepted count')
        self.assertEqual([test_spell01], slp.get_triggered_spells(), 'triggered spells')

    def test_get_hardware_hints(self):
        """ test """
        test_spell01 = Spell("Test Spell 01").set_hardware_set(['Button01'])
        test_spell02 = Spell("Test Spell 02").set_hardware_set(['Button02', 'Button03'])
        slp = SpellListPrepared('MyList').spell_add_list([test_spell01, test_spell02])
        hwl = slp.get_hardware_hints()
        self.assertTrue(set(['Button01', 'Button02', 'Button03']), set(hwl))


if __name__ == '__main__':
    unittest.main()
