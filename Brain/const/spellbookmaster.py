from spell import Spell
from const.spelltriggergestureconst import SpellTriggerGestureConst


class SpellBookMaster():

    __fireball_triggers = [SpellTriggerGestureConst.Pointing_Upwards,
      SpellTriggerGestureConst.Leaning_Forwards_Upwards,
      SpellTriggerGestureConst.Horizontal,
      SpellTriggerGestureConst.Leaning_Forwards_Downwards,
      SpellTriggerGestureConst.Pointing_Downwards ]

    Fireball = Spell("Fireball").setTriggerActions(__fireball_triggers).setTriggerTimeout(6)

