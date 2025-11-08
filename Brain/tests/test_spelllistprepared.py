"""test"""

from __future__ import absolute_import
import unittest
import logging

from brain.spelllistprepared import SpellListPrepared
from brain.spell import Spell
from brain.spelltrigger import SpellTrigger
from brain.rodevent import RodEvent
import tests

logging.basicConfig(level=logging.DEBUG)


class TestSpellListPrepared(unittest.TestCase):
    """test"""

    @classmethod
    def setUpClass(cls):
        """test"""
        cls.rod_name = "Test SpellListPrepared"

    def test_constructor(self):
        """test"""
        slp = SpellListPrepared()
        self.assertFalse(slp is None, "must not be None")

    def test_spell_add(self):
        """test"""
        slp = SpellListPrepared()
        slp_got = slp.spell_add(Spell("Test Spell 01"))
        self.assertEqual(slp, slp_got, "builder pattern. must be object")

    def test_spell_add_list(self):
        """test"""
        slp = SpellListPrepared()
        slp_got = slp.spell_add_list([Spell("Test Spell 01")])
        self.assertEqual(slp, slp_got, "builder pattern. must be object")

    def test_spell_del(self):
        """test"""
        test_spell01 = Spell("Test Spell 01")
        slp = SpellListPrepared()
        slp.spell_add_list([test_spell01])
        slp_got = slp.spell_del(test_spell01)
        self.assertEqual(slp, slp_got, "builder pattern. must be object")

    def test_receive_events_no_spells_no_events(self):
        """test"""
        slp = SpellListPrepared()
        self.assertEqual(set([]), slp.receive_events([]))

    def test_receive_events_no_spells_some_events(self):
        """test"""
        slp = SpellListPrepared()
        self.assertEqual(set([]), slp.receive_events([tests.EVENT["TEST_01"], tests.EVENT["TEST_02"]]))

    # Only accept events that are for our prepared spells
    def test_receive_events_some_spells_unwanted_events(self):
        """test"""
        test_spell01 = Spell("Test Spell 01").set_trigger_sequence([SpellTrigger("TEST_01"), SpellTrigger("TEST_02")])

        slp = SpellListPrepared().spell_add(test_spell01)
        new_events = [RodEvent("Event 03", 4)]
        self.assertEqual(set([]), slp.receive_events(new_events))

    def test_receive_events_one_spells_no_events(self):
        """test"""
        slp = SpellListPrepared().spell_add(Spell("Test Spell 01"))
        self.assertSetEqual(set([]), slp.receive_events([]))

    def test_receive_events_one_spell(self):
        """test"""
        test_spell01 = Spell("test_receives_event_one_spell").set_trigger_sequence(
            [SpellTrigger("TEST_01"), SpellTrigger("TEST_02")]
        )
        slp = SpellListPrepared().spell_add(test_spell01)
        # RodEvent TEST_03 will be ignored
        new_events = [RodEvent("TEST_01", 4), RodEvent("TEST_02", 4), RodEvent("TEST_03", 4)]
        spells_activated = slp.receive_events(new_events)
        self.assertSetEqual(set([test_spell01]), spells_activated)

    def test_receive_events_some_spells(self):
        """test"""
        test_spell01 = Spell("spell01").set_trigger_sequence([SpellTrigger("TEST_01"), SpellTrigger("TEST_03")])
        test_spell02 = Spell("spell02").set_trigger_sequence([SpellTrigger("TEST_01"), SpellTrigger("TEST_02")])
        test_spell03 = Spell("spell03").set_trigger_sequence([SpellTrigger("TEST_01"), SpellTrigger("TEST_04")])
        test_spell04 = Spell("spell04").set_trigger_sequence([SpellTrigger("TEST_02"), SpellTrigger("TEST_01")])
        slp = SpellListPrepared().spell_add_list([test_spell01, test_spell02, test_spell03, test_spell04])
        new_events = [RodEvent("TEST_01", 4), RodEvent("TEST_02", 4), RodEvent("TEST_03", 4)]
        spells_activated = slp.receive_events(new_events)
        # Note spell01 will also active because the RodEvent TEST_02 won't cancel the sequence
        self.assertSetEqual(set([test_spell01, test_spell02]), spells_activated)

    def test_get_hardware_hints(self):
        """test"""
        test_spell01 = Spell("Test Spell 01").set_trigger_sequence(
            [SpellTrigger("Trigger 01", "Button01"), SpellTrigger("Trigger 02", "Button02")]
        )
        test_spell02 = Spell("Test Spell 02").set_trigger_sequence([SpellTrigger("Trigger 03", "Button03")])
        slp = SpellListPrepared().spell_add_list([test_spell01, test_spell02])
        hwl = slp.get_hardware_hints()
        self.assertEqual(set(["Button01", "Button02", "Button03"]), set(hwl))
