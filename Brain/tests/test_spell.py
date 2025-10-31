"""test"""

from __future__ import absolute_import
import unittest

from brain.spell import Spell
from brain.rod import Rod
from brain.const import ST_GESTURE, HW_ACCELEROMETER


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
        cls.spell_trigger_timeout = 6

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
        st_got = spell.set_trigger_timeout(self.spell_trigger_timeout)
        self.assertEqual(spell, st_got)
        stt_got = spell.get_trigger_timeout()
        self.assertEqual(self.spell_trigger_timeout, stt_got)

    def test_hardware_set(self):
        """test"""
        hw_set = set([HW_ACCELEROMETER])
        spell = Spell(name=self.spell_name)
        st_got = spell.set_hardware_set(hw_set)
        self.assertEqual(spell, st_got)
        hw_got = spell.get_hardware_set()
        self.assertEqual(hw_set, hw_got)

    @staticmethod
    def spell_callback(spell: Spell, rod: Rod):
        """test"""
        print("callback spell=" + spell.get_name() + ", rod=" + rod.get_name())

    def test_perform_action(self):
        """test"""
        spell = Spell(name=self.spell_name)
        spell.set_perform_action(self.spell_callback)
        cb_got = spell.get_perform_action()
        self.assertEqual(self.spell_callback, cb_got)


if __name__ == "__main__":
    unittest.main()
