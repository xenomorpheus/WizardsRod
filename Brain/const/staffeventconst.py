
""" Simple generic events that the staff will generate and look
  for in order to trigger spells """

from staffevent import StaffEvent
from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture


class StaffEventConst():

    """ Simple generic events that the staff will generate and look
      for in order to trigger spells """

    # Only for test spells
    Test01 = StaffEvent(gesture.Test01.get_name(), 0)
    Test02 = StaffEvent(gesture.Test02.get_name(), 0)
    Test03 = StaffEvent(gesture.Test03.get_name(), 0)
