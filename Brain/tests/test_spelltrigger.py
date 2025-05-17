"""test"""

from __future__ import absolute_import
import unittest

from brain.spelltrigger import SpellTrigger
from brain.staffevent import StaffEvent
import tests


class TestSpellTrigger(unittest.TestCase):
    """test"""

    def test_constructor(self):
        """test"""
        trigger = SpellTrigger(tests.SPELL_TRIGGER_TYPE["TEST_01"])
        self.assertTrue(isinstance(trigger, SpellTrigger))

    def test_get_name(self):
        """test"""
        trigger = SpellTrigger("test trigger")
        self.assertEqual("test trigger", trigger.get_name())

    def test_get_name_with_type(self):
        """test"""
        spell_trigger_type = tests.SPELL_TRIGGER_TYPE["TEST_01"]
        trigger = SpellTrigger("test trigger", spell_trigger_type)
        self.assertEqual("test trigger", trigger.get_name())

    def test_get_trigger_type(self):
        """test"""
        spell_trigger_type = tests.SPELL_TRIGGER_TYPE["TEST_01"]
        trigger = SpellTrigger("my trigger", spell_trigger_type)
        self.assertEqual(spell_trigger_type, trigger.get_spelltrigger_type())

    def test_equal(self):
        """test"""
        spell_trigger1 = SpellTrigger("trigger 01", tests.SPELL_TRIGGER_TYPE["TEST_01"])
        spell_trigger2 = SpellTrigger("trigger 01", tests.SPELL_TRIGGER_TYPE["TEST_01"])
        spell_trigger3 = SpellTrigger("trigger 02", tests.SPELL_TRIGGER_TYPE["TEST_02"])
        self.assertEqual(spell_trigger1, spell_trigger2)
        self.assertNotEqual(spell_trigger1, spell_trigger3)

    def test_eq_not_implemented(self):
        """test"""
        spell_trigger1 = SpellTrigger("trigger 01", tests.SPELL_TRIGGER_TYPE["TEST_01"])
        result = spell_trigger1.__eq__("Non SpellTrigger")
        assert result is NotImplemented

    def test_hash(self):
        """test"""
        spell_trigger1 = SpellTrigger("trigger 01", tests.SPELL_TRIGGER_TYPE["TEST_01"])
        spell_trigger2 = SpellTrigger("trigger 01", tests.SPELL_TRIGGER_TYPE["TEST_01"])
        spell_trigger3 = SpellTrigger("trigger 02", tests.SPELL_TRIGGER_TYPE["TEST_02"])
        self.assertEqual(hash(spell_trigger1), hash(spell_trigger2), "hash spell_trigger1 and spell_trigger2")
        self.assertNotEqual(hash(spell_trigger1), hash(spell_trigger3), "hash spell_trigger1 and spell_trigger3")

    def test_is_triggerd_by(self):
        """test"""
        trigger = SpellTrigger("TEST_01")
        event = StaffEvent("TEST_01")
        self.assertTrue(trigger.is_triggerd_by(event))

    def test_is_triggerd_by_with_type(self):
        """test"""
        trigger = SpellTrigger("TEST_01", spelltrigger_type="foo")
        event = StaffEvent("TEST_01", staffevent_type="foo")
        self.assertTrue(trigger.is_triggerd_by(event))

    def test_is_triggerd_by_with_wrong_type(self):
        """test"""
        trigger = SpellTrigger("TEST_01", spelltrigger_type="foo")
        event = StaffEvent("TEST_01", staffevent_type="wrong")
        self.assertFalse(trigger.is_triggerd_by(event))


if __name__ == "__main__":
    unittest.main()
