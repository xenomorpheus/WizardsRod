""" test """
from __future__ import absolute_import
import unittest

from staffevent import StaffEvent
from const.spelltriggertypeconst import SpellTriggerTypeConst as trigger_type


class TestStaffEvent(unittest.TestCase):
    """ test """

    def test_constructor(self):
        """ test """
        staff_event = StaffEvent(trigger_type.Test01, 0)
        self.assertTrue(isinstance(staff_event, StaffEvent))

    def test_get_event_type(self):
        """ test """
        staff_event = StaffEvent(trigger_type.Test01, 0)
        self.assertEqual(trigger_type.Test01, staff_event.get_event_type())

    def test_get_created(self):
        """ test """
        staff_event = StaffEvent(trigger_type.Test01, 99)
        self.assertEqual(99, staff_event.get_created())

    def test_equal(self):
        """ test """
        staff_event1 = StaffEvent(trigger_type.Test01, 4)
        staff_event2 = StaffEvent(trigger_type.Test01, 4)
        staff_event3 = StaffEvent(trigger_type.Test02, 4)
        self.assertTrue(staff_event1.__eq__(staff_event2))
        self.assertEqual(staff_event1, staff_event2)
        self.assertNotEqual(staff_event1, staff_event3)

    def test_hash(self):
        """ test """
        staff_event1 = StaffEvent(trigger_type.Test01, 4)
        staff_event2 = StaffEvent(trigger_type.Test01, 4)
        staff_event3 = StaffEvent(trigger_type.Test02, 4)
        self.assertEqual(staff_event1.__hash__(), staff_event2.__hash__(),
                         'hash staff_event1 and staff_event2')
        self.assertNotEqual(staff_event1.__hash__(), staff_event3.__hash__(),
                            'hash staff_event1 and staff_event3')


if __name__ == '__main__':
    unittest.main()
