"""test"""

from __future__ import absolute_import
import unittest

from brain.spell import Spell
from brain.const import ST_GESTURE


class TestSpellTrigger(unittest.TestCase):
    """test"""

    @classmethod
    def setUpClass(cls):
        cls.spell_name = "Test Spell"
        cls.spell_trigger_list = [
            ST_GESTURE["POINTING_UPWARDS"],
            ST_GESTURE["LEANING_FORWARDS_UPWARDS"],
            ST_GESTURE["HORIZONTAL"],
            ST_GESTURE["LEANING_FORWARDS_DOWNWARDS"],
            ST_GESTURE["POINTING_DOWNWARDS"],
        ]
        cls.trigger_timeout = 6

    def test_constructor(self):
        """test"""
        spell = Spell(name=self.spell_name)
        self.assertTrue(isinstance(spell, Spell))

    def test_get_name(self):
        """test"""
        spell = Spell(name=self.spell_name)
        self.assertEqual(self.spell_name, spell.get_name())

    def test_trigger_sequence(self):
        """test"""
        spell = Spell(name=self.spell_name)
        st_got = spell.set_trigger_sequence(self.spell_trigger_list)
        self.assertEqual(spell, st_got)
        sta_got = spell.get_trigger_sequence()
        self.assertEqual(self.spell_trigger_list, sta_got)

    def test_trigger_timeout(self):
        """test"""
        spell = Spell(name=self.spell_name)
        st_got = spell.set_trigger_timeout(self.trigger_timeout)
        self.assertEqual(spell, st_got)
        tt_got = spell.get_trigger_timeout()
        self.assertEqual(self.trigger_timeout, tt_got)

    def test_perform_action(self):
        """test"""
        spell = Spell(name=self.spell_name)
        # we just need a callable for this test. Don't define one as it won't be called and will reduce coverage.
        spell.set_perform_action(self.test_perform_action)
        action_got = spell.get_perform_action()
        self.assertEqual(self.test_perform_action, action_got)
