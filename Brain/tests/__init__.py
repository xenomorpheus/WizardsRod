# Only for tests.
from staffevent import StaffEvent
from spelltrigger import SpellTrigger
from spell import Spell
import const

# Spell triggers that trigger a spell event

_STT_TEST01 = "TEST_01"
_STT_TEST02 = "TEST_02"
_STT_TEST03 = "TEST_03"

SPELL_TRIGGER_TYPE = {_STT_TEST01: _STT_TEST01,
                      _STT_TEST02: _STT_TEST02,
                      _STT_TEST03: _STT_TEST03, }

# Simple generic events that the staff will generate and look
#  for in order to trigger spells.

_SE_TEST_01 = StaffEvent(_STT_TEST01, 0)
_SE_TEST_01 = StaffEvent(_STT_TEST02, 0)
_SE_TEST_03 = StaffEvent(_STT_TEST03, 0)

EVENT = {_STT_TEST01: _SE_TEST_01,
         _STT_TEST03: _SE_TEST_01,
         _STT_TEST02: _SE_TEST_03}

# TestSpells are only for unit tests

_SPELL_TEST_01_TRIGGERS = [
    SpellTrigger('test trigger 01', _STT_TEST01),
    SpellTrigger('test trigger 02', _STT_TEST02),
    SpellTrigger('test trigger 03', _STT_TEST03)]
_SPELL_TEST_STR_01 = "TEST_SPELL_01"
_SPELL_TEST_01 = Spell(_SPELL_TEST_STR_01).set_trigger_sequence(
    _SPELL_TEST_01_TRIGGERS).set_trigger_timeout(6) \
    .set_hardware_set(set(const.HW_ACCELEROMETER))

# A master list of spells.
# TODO MASTER_SPELLBOOK = {_SPELL_TEST_STR_01: _SPELL_TEST_01}