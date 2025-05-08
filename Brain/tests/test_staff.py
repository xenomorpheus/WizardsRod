""" test """
from __future__ import absolute_import
import unittest

from staff import Staff
from spell import Spell


class TestStaff(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ test """
        cls.staff_name = "Test Staff"

    def test_constructor(self):
        """ test """
        staff = Staff(name=self.staff_name)
        self.assertTrue(isinstance(staff, Staff))

    def test_get_name(self):
        """ test """
        staff = Staff(name=self.staff_name)
        self.assertEqual(self.staff_name, staff.get_name())

    def test_spell_add(self):
        """ test """
        staff = Staff(name=self.staff_name)
        spell = Spell(name="spell name 01")
        got = staff.spell_add(spell)
        self.assertEqual(staff, got, "return staff")

    def test_spell_add_list(self):
        """ test """
        staff = Staff(name=self.staff_name)
        spell1 = Spell(name="spell name 01")
        spell2 = Spell(name="spell name 02")
        spell_list = [spell1, spell2]
        got = staff.spell_add_list(spell_list)
        self.assertEqual(staff, got, "return staff")

    def test_run(self):
        """ test """
        staff = Staff(name=self.staff_name)
        spell = Spell(name="spell name 01")
        staff.spell_add(spell)
        staff.run()


if __name__ == '__main__':
    unittest.main()
