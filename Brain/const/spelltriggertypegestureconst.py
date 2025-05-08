
""" spell trigger that are gestures AKA movement """

from spelltriggertypegesture import SpellTriggerTypeGesture


class SpellTriggerTypeGestureConst():
    """ spell trigger that are gestures AKA movement """

    Pointing_Upwards = SpellTriggerTypeGesture("Pointing upwards")
    Leaning_Forwards_Upwards = SpellTriggerTypeGesture("Leaning forwards upwards")
    Horizontal = SpellTriggerTypeGesture("Horizontal")
    Leaning_Forwards_Downwards = SpellTriggerTypeGesture("Leaning forwards downwards")
    Pointing_Downwards = SpellTriggerTypeGesture("Pointing downwards")

    # Only for tests.
    Test01 = SpellTriggerTypeGesture("Test Gesture 01")
    Test02 = SpellTriggerTypeGesture("Test Gesture 02")
    Test03 = SpellTriggerTypeGesture("Test Gesture 03")
