"""test"""

from __future__ import absolute_import
import unittest
import logging

from brain.rod import Rod
from brain.spell import Spell
from brain.spelltrigger import SpellTrigger
from brain.rodevent import RodEvent
from brain.hardware import Hardware

logging.basicConfig(level=logging.DEBUG)


class FakeHardware(Hardware):
    """
    Send RodEvent objects to listeners that have been previously setup.
    """

    def __init__(self):
        """Constructor"""
        super().__init__(self, "none")

    def generate_events(self, events) -> None:
        """generate events to send to listeners"""
        for listener in self.listeners:
            listener.receive_events(events)


class TestRod(unittest.TestCase):
    """test"""

    @classmethod
    def setUpClass(cls):
        """test"""
        cls.rod_name = "Test Rod"
        cls.logger = logging.getLogger(__name__)

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

    def test_spell_del_with_hardware(self):
        """test"""
        rod = Rod(name=self.rod_name)

        # setup fake hardware and register it with the rod
        hwf = rod.testing_get_hwf()
        fake_hw = FakeHardware()
        hwf.set(fake_hw.get_hardware_type(), fake_hw)

        spell = Spell(name="spell name 01").set_trigger_sequence([SpellTrigger("TEST_01")])
        rod.spell_add(spell)
        got = rod.spell_del(spell)
        self.assertEqual(rod, got, "return rod")

    def test_spell_activate(self):
        """test that a spell is activated by events"""

        # keep track of last arguments passed to action
        last_args = {}

        def action(spell, rod):
            last_args.update({"spell": spell, "rod": rod})

        rod = Rod(name=self.rod_name)

        # setup fake hardware and register it with the rod
        hwf = rod.testing_get_hwf()
        fake_hw = FakeHardware()
        hwf.set(fake_hw.get_hardware_type(), fake_hw)

        # create a spell that is activated by events
        test_spell01 = Spell(name="spell name 01")
        test_spell01.set_perform_action(action)
        test_spell01.set_trigger_sequence([SpellTrigger("TEST_01"), SpellTrigger("TEST_02")])

        rod.spell_add(test_spell01)

        # the rod will to listen for the events. Gesture TEST_03 will be ignored
        new_events = [RodEvent("TEST_01", 4), RodEvent("TEST_02", 4), RodEvent("TEST_03", 4)]

        # Fake hardware sends the events to the rod
        fake_hw.generate_events(new_events)

        # check that the spell was activated
        self.assertEqual(test_spell01, last_args.get("spell"))
        self.assertEqual(rod, last_args.get("rod"))

    def test_end(self):
        """test"""
        rod = Rod(name=self.rod_name)
        rod.end()

    def test_end_with_hardware(self):
        """test"""
        rod = Rod(name=self.rod_name)

        # setup fake hardware and register it with the rod
        hwf = rod.testing_get_hwf()
        fake_hw = FakeHardware()
        hwf.set(fake_hw.get_hardware_type(), fake_hw)

        spell = Spell(name="spell name 01").set_trigger_sequence([SpellTrigger("TEST_01")])
        rod.spell_add(spell)
        rod.end()
