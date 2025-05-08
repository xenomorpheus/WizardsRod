
""" Simple generic events that the staff will generate and look
  for in order to trigger spells """

from staffevent import StaffEvent
from const.spelltriggertypeconst import SpellTriggerTypeConst as trigger_type


class StaffEventConst():

    """ Simple generic events that the staff will generate and look
      for in order to trigger spells """

    # Only for test spells
    Test01 = StaffEvent(trigger_type.Test01, 0)
    Test02 = StaffEvent(trigger_type.Test02, 0)
    Test03 = StaffEvent(trigger_type.Test03, 0)
