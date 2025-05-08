import unittest

from spelllistprepared import SpellListPrepared
from spell import Spell
from staffevent import StaffEvent
from const.spellbookmaster import SpellBookMaster
from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture
from const.staffeventconst import StaffEventConst as event


class TestSpellListPrepared(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spell = SpellBookMaster.TestSpell01

    def test_constructor(self):
        self.longMessage=True
        slp = SpellListPrepared(name='MyList')
        self.assertFalse(slp is None, 'must not be None')

    def test_getName(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList')
        self.assertEqual('MyList', slp.getName())

    def test_spellAdd(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList')
        slp_got = slp.spellAdd(self.spell)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spellAddList(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList')
        slp_got = slp.spellAddList([self.spell])
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spellDel(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList')
        slp_got = slp.spellDel(self.spell.name)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_acceptEvents_no_spells_no_events(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList')
        new_events = []
        accepted_count = slp.acceptEvents(new_events)
        self.assertEqual(0, accepted_count)

    def test_acceptEvents_no_spells_some_events(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList')
        new_events = [event.Test01, event.Test02]
        accepted_count = slp.acceptEvents(new_events)
        self.assertEqual(0, accepted_count)

    def test_acceptEvents_some_spells_some_events(self):
        self.longMessage=True
        triggers = [gesture.Test01, gesture.Test02 ]
        TestSpell01 = Spell("Test Spell 01").setTriggerList(triggers)
        slp = SpellListPrepared('MyList').spellAdd(TestSpell01)
        # 03 ignored
        events = [
            StaffEvent("Event 01", gesture.Test01, 4),
            StaffEvent("Event 02", gesture.Test02, 4),
            StaffEvent("Event 03", gesture.Test03, 4)]
        accepted_count = slp.acceptEvents(events)
        self.assertEqual(2, accepted_count, 'accepted count')

    # Only accept events that are for our prepared spells
    def test_acceptEvents_some_spells_unwanted_events(self):
        self.longMessage=True
        triggers = [gesture.Test01, gesture.Test02 ]
        TestSpell01 = Spell("Test Spell 01").setTriggerList(triggers)
        slp = SpellListPrepared('MyList').spellAdd(TestSpell01)
        events = [
            StaffEvent("Event 03", gesture.Test03, 4)]
        accepted_count_got = slp.acceptEvents(events)
        self.assertEqual(0, accepted_count_got, 'accepted count')

    def test_getTriggeredSpells_no_spells_no_events(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList')
        new_events = []
        slp.acceptEvents(new_events)
        triggerd_spells = slp.getTriggeredSpells()
        self.assertEqual([], triggerd_spells)

    def test_getTriggeredSpells_one_spells_no_events(self):
        self.longMessage=True
        slp = SpellListPrepared('MyList').spellAdd(self.spell)
        new_events = []
        slp.acceptEvents(new_events)
        triggerd_spells = slp.getTriggeredSpells()
        self.assertEqual([], triggerd_spells, 'no triggered spells')

    def test_getTriggeredSpells_some_spells(self):
        self.longMessage=True
        triggers = [gesture.Test01, gesture.Test02 ]
        TestSpell01 = Spell("Test Spell 01").setTriggerList(triggers)
        slp = SpellListPrepared('MyList').spellAdd(TestSpell01)
        # 03 ignored
        events = [
            StaffEvent("Event 01", gesture.Test01, 4),
            StaffEvent("Event 02", gesture.Test02, 4),
            StaffEvent("Event 03", gesture.Test03, 4)]
        accepted_count = slp.acceptEvents(events)
        self.assertEqual(2, accepted_count, 'accepted count')

        self.assertEqual([TestSpell01], slp.getTriggeredSpells(), 'triggered spells')


if __name__ == '__main__':
    unittest.main()
