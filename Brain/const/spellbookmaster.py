
""" A master list of spells """

from spell import Spell
from spelltrigger import SpellTrigger
from const.spelltriggertypeconst import SpellTriggerTypeConst as trigger_type
from const.spellhardwareconst import SpellHardwareConst as hw


class SpellBookMaster():

    """ TestSpells are only for unit tests """

    __test_spell_01_triggers = [
        SpellTrigger(trigger_type.Test01),
        SpellTrigger(trigger_type.Test02),
        SpellTrigger(trigger_type.Test03)]
    TestSpell01 = Spell("Test Spell 01").set_trigger_sequence(
        __test_spell_01_triggers).set_trigger_timeout(6) \
        .set_hardware_set([hw.ACCELEROMETER])
