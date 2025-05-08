from spell import Spell
from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture
from const.spellhardwareconst import SpellHardwareConst as hw


class SpellBookMaster():

    __test_spell_01_triggers = [gesture.Test01, gesture.Test02, gesture.Test03 ]
    TestSpell01 = Spell("Test Spell 01").setTriggerSequence(__test_spell_01_triggers).setTriggerTimeout(6) \
        .setHardwareSet([hw.ACCELEROMETER])
