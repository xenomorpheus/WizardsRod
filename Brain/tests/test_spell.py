import unittest

from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture
from const.spellhardwareconst import SpellHardwareConst as hw
from spell import Spell


class TestSpellTrigger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.name = "Test Spell"
        cls.spell_trigger_list = [gesture.Pointing_Upwards,
          gesture.Leaning_Forwards_Upwards,
          gesture.Horizontal,
          gesture.Leaning_Forwards_Downwards,
          gesture.Pointing_Downwards ]
        cls.spell_trigger_timeout = 6

    def test_constructor(self):
        st = Spell(name=self.name)

    def test_getName(self):
        st = Spell(name=self.name)
        self.assertEqual(self.name, st.getName())

    def test_TriggerList(self):
        st = Spell(name=self.name)
        st_got = st.setTriggerList(self.spell_trigger_list)
        self.assertEqual(st, st_got)
        sta_got = st.getTriggerList()
        self.assertEqual(self.spell_trigger_list, sta_got)

    def test_TriggerTimeout(self):
        st = Spell(name=self.name)
        st_got = st.setTriggerTimeout(self.spell_trigger_timeout)
        self.assertEqual(st, st_got)
        stt_got = st.getTriggerTimeout()
        self.assertEqual(self.spell_trigger_timeout, stt_got)

    def test_HardwareList(self):
        hwlist = [hw.ACCELEROMETER]
        st = Spell(name=self.name)
        st_got = st.setHardwareList(hwlist)
        self.assertEqual(st, st_got)
        hw_got = st.getHardwareList()
        self.assertEqual(hwlist, hw_got)


if __name__ == '__main__':
    unittest.main()
