
""" spell trigger that are gestures AKA movement """

from spelltriggergesture import SpellTriggerGesture


class SpellTriggerGestureConst():
    """ spell trigger that are gestures AKA movement """

    Pointing_Upwards = SpellTriggerGesture("Pointing upwards")
    Leaning_Forwards_Upwards = SpellTriggerGesture("Leaning forwards upwards")
    Horizontal = SpellTriggerGesture("Horizontal")
    Leaning_Forwards_Downwards = SpellTriggerGesture("Leaning forwards downwards")
    Pointing_Downwards = SpellTriggerGesture("Pointing downwards")

    # Only for tests.
    Test01 = SpellTriggerGesture("Test Gesture 01")
    Test02 = SpellTriggerGesture("Test Gesture 02")
    Test03 = SpellTriggerGesture("Test Gesture 03")
