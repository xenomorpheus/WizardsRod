""" test """
from __future__ import absolute_import
import unittest

from spell import Spell
from staff import Staff
import const


class TestSpellTrigger(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        cls.spell_name = 'Test Spell'
        cls.spell_trigger_list = [const.ST_GESTURE['POINTING_UPWARDS'],
                                  const.ST_GESTURE['LEANING_FORWARDS_UPWARDS'],
                                  const.ST_GESTURE['HORIZONTAL'],
                                  const.
                                  ST_GESTURE['LEANING_FORWARDS_DOWNWARDS'],
                                  const.ST_GESTURE['POINTING_DOWNWARDS']]
        cls.spell_trigger_timeout = 6

    def test_constructor(self):
        """ test """
        spell = Spell(name=self.spell_name)
        self.assertTrue(isinstance(spell, Spell))

    def test_get_name(self):
        """ test """
        spell = Spell(name=self.spell_name)
        self.assertEqual(self.spell_name, spell.get_name())

    def test_trigger_sequence(self):
        """ test """
        spell = Spell(name=self.spell_name)
        st_got = spell.set_trigger_sequence(self.spell_trigger_list)
        self.assertEqual(spell, st_got)
        sta_got = spell.get_trigger_sequence()
        self.assertEqual(self.spell_trigger_list, sta_got)

    def test_trigger_timeout(self):
        """ test """
        spell = Spell(name=self.spell_name)
        st_got = spell.set_trigger_timeout(self.spell_trigger_timeout)
        self.assertEqual(spell, st_got)
        stt_got = spell.get_trigger_timeout()
        self.assertEqual(self.spell_trigger_timeout, stt_got)

    def test_hardware_set(self):
        """ test """
        hwlist = [const.HW_ACCELEROMETER]
        spell = Spell(name=self.spell_name)
        st_got = spell.set_hardware_set(hwlist)
        self.assertEqual(spell, st_got)
        hw_got = spell.get_hardware_set()
        self.assertEqual(hwlist, hw_got)

    @staticmethod
    def spell_callback(spell: Spell, staff: Staff):
        """ test """
        print("callback spell="+spell.get_name()+", staff="+staff.get_name())

    def test_perform_actions(self):
        """ test """
        spell = Spell(name=self.spell_name)
        spell.set_perform_actions(self.spell_callback)
        staff = Staff("some staff")
        spell.perform_actions(staff)


if __name__ == '__main__':
    unittest.main()
