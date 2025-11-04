"""test"""

from __future__ import absolute_import
import unittest
import logging

from brain.rod import Rod
from brain.spell import Spell


class TestRod(unittest.TestCase):
    """test"""

    @classmethod
    def setUpClass(cls):
        """test"""
        cls.rod_name = "Test Rod"
        logging.basicConfig(level=logging.DEBUG)

    def test_constructor(self):
        """test"""
        rod = Rod(name=self.rod_name)
        self.assertTrue(isinstance(rod, Rod))

    def test_get_name(self):
        """test"""
        rod = Rod(name=self.rod_name)
        self.assertEqual(self.rod_name, rod.get_name())

    def test_spell_add(self):
        """test"""
        rod = Rod(name=self.rod_name)
        spell = Spell(name="spell name 01")
        got = rod.spell_add(spell)
        self.assertEqual(rod, got, "return rod")

    def test_spell_add_list(self):
        """test"""
        rod = Rod(name=self.rod_name)
        spell1 = Spell(name="spell name 01")
        spell2 = Spell(name="spell name 02")
        spell_list = [spell1, spell2]
        got = rod.spell_add_list(spell_list)
        self.assertEqual(rod, got, "return rod")

    def test_spell_del(self):
        """test"""
        rod = Rod(name=self.rod_name)
        spell = Spell(name="spell name 01")
        rod.spell_add(spell)
        got = rod.spell_del(spell)
        self.assertEqual(rod, got, "return rod")

    def test_spell_activate(self):
        """test that a spell is activated by events"""
        # TODO create a spell that is activated by an event
        # TODO get the rod to listen for the event
        # TODO send the event
        # TODO check the spell activated
        rod = Rod(name=self.rod_name)
        spell = Spell(name="spell name 01")
        rod.spell_add(spell)
        # TODO lots

    def test_end(self):
        """end"""
        rod = Rod(name=self.rod_name)
        rod.end()

    def test_end_with_hardware(self):
        """end"""
        rod = Rod(name=self.rod_name)
        spell = Spell(name="spell name 01")
        #        spell.set_hardware_set([const.HW_BUTTON])
        rod.spell_add(spell)
        rod.end()
