""" test """
from __future__ import absolute_import
import unittest

from staff import Staff


class TestStaff(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ test """
        cls.name = "Test Staff"

    def test_constructor(self):
        """ test """
        staff = Staff(name=self.name)
        self.assertTrue(isinstance(staff, Staff))

    def test_get_name(self):
        """ test """
        staff = Staff(name=self.name)
        self.assertEqual(self.name, staff.get_name())


if __name__ == '__main__':
    unittest.main()
