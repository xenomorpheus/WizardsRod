"""Constants. Only for tests"""

from brain.rodevent import RodEvent
from brain.spelltrigger import SpellTrigger
from brain.spell import Spell
from brain.const import HW_ACCELEROMETER

# Spell triggers that trigger a spell event

_TT_TEST01 = "TEST_01"
_TT_TEST02 = "TEST_02"
_TT_TEST03 = "TEST_03"

TRIGGER_TYPE = {
    _TT_TEST01: _TT_TEST01,
    _TT_TEST02: _TT_TEST02,
    _TT_TEST03: _TT_TEST03,
}

# Simple generic events that the rod will generate and look
#  for in order to trigger spells.

_SE_TEST_01 = RodEvent(_TT_TEST01, 0)
_SE_TEST_01 = RodEvent(_TT_TEST02, 0)
_SE_TEST_03 = RodEvent(_TT_TEST03, 0)

EVENT = {_TT_TEST01: _SE_TEST_01, _TT_TEST03: _SE_TEST_01, _TT_TEST02: _SE_TEST_03}

# TestSpells are only for unit tests

_SPELL_TEST_01_TRIGGERS = [
    SpellTrigger("test trigger 01", _TT_TEST01),
    SpellTrigger("test trigger 02", _TT_TEST02),
    SpellTrigger("test trigger 03", _TT_TEST03),
]
_SPELL_TEST_STR_01 = "TEST_SPELL_01"
_SPELL_TEST_01 = Spell(_SPELL_TEST_STR_01).set_trigger_sequence(_SPELL_TEST_01_TRIGGERS).set_trigger_timeout(6)

# A master list of spells.
# TODO MASTER_SPELLBOOK = {_SPELL_TEST_STR_01: _SPELL_TEST_01}
