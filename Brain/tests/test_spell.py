import unittest

from const.spelltriggergestureconst import SpellTriggerGestureConst
from spell import Spell


class TestSpellTrigger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.name = "Fireball"
        cls.spell_trigger_actions = [SpellTriggerGestureConst.Pointing_Upwards,
          SpellTriggerGestureConst.Leaning_Forwards_Upwards,
          SpellTriggerGestureConst.Horizontal,
          SpellTriggerGestureConst.Leaning_Forwards_Downwards,
          SpellTriggerGestureConst.Pointing_Downwards ]
        cls.spell_trigger_timeout = 6

    def test_constructor(self):
        st = Spell(name=self.name, spell_trigger_actions=self.spell_trigger_actions, spell_trigger_timeout=self.spell_trigger_timeout)

    def test_getName(self):
        st = Spell(name=self.name, spell_trigger_actions=self.spell_trigger_actions, spell_trigger_timeout=self.spell_trigger_timeout)
        self.assertEqual(self.name, st.getName())

if __name__ == '__main__':
    unittest.main()
