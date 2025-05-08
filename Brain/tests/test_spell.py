""" test """
from __future__ import absolute_import
import unittest

from const.spelltriggertypegestureconst import SpellTriggerTypeGestureConst as gesture
from const.spellhardwareconst import SpellHardwareConst as hw
from spell import Spell


class TestSpellTrigger(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        cls.name = "Test Spell"
        cls.spell_trigger_list = [gesture.Pointing_Upwards,
                                  gesture.Leaning_Forwards_Upwards,
                                  gesture.Horizontal,
                                  gesture.Leaning_Forwards_Downwards,
                                  gesture.Pointing_Downwards]
        cls.spell_trigger_timeout = 6

    def test_constructor(self):
        """ test """
        spell = Spell(name=self.name)
        self.assertTrue(isinstance(spell, Spell))

    def test_get_name(self):
        """ test """
        spell = Spell(name=self.name)
        self.assertEqual(self.name, spell.get_name())

    def test_trigger_sequence(self):
        """ test """
        spell = Spell(name=self.name)
        st_got = spell.set_trigger_sequence(self.spell_trigger_list)
        self.assertEqual(spell, st_got)
        sta_got = spell.get_trigger_sequence()
        self.assertEqual(self.spell_trigger_list, sta_got)

    def test_trigger_timeout(self):
        """ test """
        spell = Spell(name=self.name)
        st_got = spell.set_trigger_timeout(self.spell_trigger_timeout)
        self.assertEqual(spell, st_got)
        stt_got = spell.get_trigger_timeout()
        self.assertEqual(self.spell_trigger_timeout, stt_got)

    def test_hardware_set(self):
        """ test """
        hwlist = [hw.ACCELEROMETER]
        spell = Spell(name=self.name)
        st_got = spell.set_hardware_set(hwlist)
        self.assertEqual(spell, st_got)
        hw_got = spell.get_hardware_set()
        self.assertEqual(hwlist, hw_got)


if __name__ == '__main__':
    unittest.main()
