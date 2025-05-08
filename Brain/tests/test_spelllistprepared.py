import unittest

from spelllistprepared import SpellListPrepared
from const.spellbookmaster import SpellBookMaster
from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture


class TestSpellTrigger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spell = SpellBookMaster.Fireball

    def test_constructor(self):
        slp = SpellListPrepared(name='MyList')
        self.assertFalse(slp is None, 'must not be None')

    def test_getName(self):
        slp = SpellListPrepared('MyList')
        self.assertEqual('MyList', slp.getName())

    def test_spellAdd(self):
        slp = SpellListPrepared('MyList')
        slp_got = slp.spellAdd(self.spell)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spellAddList(self):
        slp = SpellListPrepared('MyList')
        slp_got = slp.spellAddList([self.spell])
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_spellDel(self):
        slp = SpellListPrepared('MyList')
        slp_got = slp.spellDel(self.spell.getName)
        self.assertEqual(slp, slp_got, 'builder pattern. must be object')

    def test_acceptActions_no_spells_no_actions(self):
        slp = SpellListPrepared('MyList')
        new_actions = []
        accepted_count = slp.acceptActions(new_actions)
        self.assertEqual(0, accepted_count)

    def test_acceptActions_no_spells_some_actions(self):
        slp = SpellListPrepared('MyList')
        new_actions = [gesture.Pointing_Downwards, gesture.Pointing_Upwards]
        accepted_count = slp.acceptActions(new_actions)
        self.assertEqual(0, accepted_count)

    def test_acceptActions_some_spells_some_actions(self):
        slp = SpellListPrepared('MyList')
        slp.spellAdd(self.spell)
        acts = self.spell.getTriggerActions()
        new_actions = []
        if (len(acts) < 2):
            self.fail('Test setup failure: no actions for spell '.self.spell)
        new_actions.append(acts[0])
        new_actions.append(acts[1])
        accepted_count = slp.acceptActions(new_actions)
        self.assertEqual(len(new_actions), accepted_count, 'action count')

    # Only accept actions that are for our prepared spells
    def test_acceptActions_some_spells_unwanted_actions(self):
        slp = SpellListPrepared('MyList')
        slp.spellAdd(self.spell)
        acts = self.spell.getTriggerActions()
        new_actions = [gesture.Testing_Only]
        accepted_count_got = slp.acceptActions(new_actions)
        self.assertEqual(0, accepted_count_got, 'action count')

    def test_getTriggeredSpells_no_spells_no_actions(self):
        slp = SpellListPrepared('MyList')
        new_actions = []
        slp.acceptActions(new_actions)
        triggerd_spells = slp.getTriggeredSpells()
        self.assertEqual([], triggerd_spells)

    def test_getTriggeredSpells_one_spells_no_actions(self):
        slp = SpellListPrepared('MyList')
        slp.spellAdd(self.spell)
        new_actions = []
        slp.acceptActions(new_actions)
        triggerd_spells = slp.getTriggeredSpells()
        self.assertEqual([], triggerd_spells, 'no triggerd spells')

    # TODO not complete
    # TODO more
    def test_getTriggeredSpells_some_spells(self):
        slp = SpellListPrepared('MyList')
        slp.spellAdd(self.spell)
        acts = self.spell.getTriggerActions()
        new_actions = []
        new_actions.extend(acts)
        slp.acceptActions(new_actions)
        triggerd_spells = slp.getTriggeredSpells()
        self.assertEqual([self.spell], triggerd_spells, 'triggered spells')  # TODO


if __name__ == '__main__':
    unittest.main()
