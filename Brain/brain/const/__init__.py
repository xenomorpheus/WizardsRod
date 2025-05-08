""" constants """

from spell import Spell
from spelltrigger import SpellTrigger
from spelltriggerbutton import SpellTriggerButton
from spelltriggergesture import SpellTriggerGesture
from staffevent import StaffEvent

# Will probably need to turn these into objects rather than strings.
# Will need to be able to select polling frequency.

_HW_GPS = "GPS"
HW_ACCELEROMETER = "ACCELEROMETER"
_HW_BUTTON = "BUTTON"

HARDWARE = {_HW_GPS: _HW_GPS,
            HW_ACCELEROMETER: HW_ACCELEROMETER,
            _HW_BUTTON: _HW_BUTTON}

# Generic spell trigger objects

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

_B_1 = SpellTriggerButton('1')
_B_2 = SpellTriggerButton('2')
_B_3 = SpellTriggerButton('3')
_B_4 = SpellTriggerButton('4')

ST_BUTTON = {'BUTTON1': _B_1,
             'BUTTON2': _B_2,
             'BUTTON3': _B_3,
             'BUTTON4': _B_4, }

