""" constants """

from spell import Spell
from spelltrigger import SpellTrigger
from spelltriggertype import SpellTriggerType
from spelltriggergesture import SpellTriggerGesture
from staffevent import StaffEvent

# Will probably need to turn these into objects rather than strings.
# Will need to be able to select polling frequency.

_HW_GPS = "GPS"
_HW_ACCELEROMETER = "ACCELEROMETER"

HARDWARE = {_HW_GPS: _HW_GPS,
            _HW_ACCELEROMETER: _HW_ACCELEROMETER}

# Generic spell trigger objects

# Only for tests.
_TRIGGER_TYPE_STR01 = "TEST_01"
_TRIGGER_TYPE_STR02 = "TEST_02"
_TRIGGER_TYPE_STR03 = "TEST_03"
_STT_TEST01 = SpellTriggerType(_TRIGGER_TYPE_STR01)
_STT_TEST02 = SpellTriggerType(_TRIGGER_TYPE_STR02)
_STT_TEST03 = SpellTriggerType(_TRIGGER_TYPE_STR03)

SPELL_TRIGGER_TYPE = {_STT_TEST01.get_name(): _STT_TEST01,
                      _STT_TEST02.get_name(): _STT_TEST02,
                      _STT_TEST03.get_name(): _STT_TEST03, }

# spell trigger that are gestures AKA movement
_G_POINTING_UPWARDS = SpellTriggerGesture("POINTING_UPWARDS")
_G_LEANING_FORWARDS_UPWARDS = SpellTriggerGesture(
    "LEANING_FORWARDS_UPWARDS")
_G_HORIZONTAL = SpellTriggerGesture("HORIZONTAL")
_G_LEANING_FORWARDS_DOWNWARDS = SpellTriggerGesture(
    "LEANING_FORWARDS_DOWNWARDS")
_G_POINTING_DOWNWARDS = SpellTriggerGesture("POINTING_DOWNWARDS")

ST_GESTURE = {'POINTING_UPWARDS': _G_POINTING_UPWARDS,
              'LEANING_FORWARDS_UPWARDS': _G_LEANING_FORWARDS_UPWARDS,
              'HORIZONTAL': _G_HORIZONTAL,
              'LEANING_FORWARDS_DOWNWARDS': _G_LEANING_FORWARDS_DOWNWARDS,
              'POINTING_DOWNWARDS': _G_POINTING_DOWNWARDS}

# Simple generic events that the staff will generate and look
#  for in order to trigger spells.

# Only for test spells
_SE_TEST_01 = StaffEvent(_STT_TEST01, 0)
_SE_TEST_02 = StaffEvent(_STT_TEST02, 0)
_SE_TEST_03 = StaffEvent(_STT_TEST03, 0)

EVENT = {_TRIGGER_TYPE_STR01: _STT_TEST01,
         _TRIGGER_TYPE_STR02: _STT_TEST02,
         _TRIGGER_TYPE_STR03: _STT_TEST03}

# A master list of spells.
# TestSpells are only for unit tests

_SPELL_TEST_01_TRIGGERS = [
    SpellTrigger('test trigger 01', _STT_TEST01),
    SpellTrigger('test trigger 02', _STT_TEST02),
    SpellTrigger('test trigger 03', _STT_TEST03)]
_SPELL_TEST_STR_01 = "TEST_SPELL_01"
_SPELL_TEST_01 = Spell(_SPELL_TEST_STR_01).set_trigger_sequence(
    _SPELL_TEST_01_TRIGGERS).set_trigger_timeout(6) \
    .set_hardware_set([_HW_ACCELEROMETER])

MASTER_SPELLBOOK = {_SPELL_TEST_STR_01: _SPELL_TEST_01}
