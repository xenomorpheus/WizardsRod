from spell import Spell
from const.spelltriggergestureconst import SpellTriggerGestureConst


class SpellBookMaster():

    __triggers = [SpellTriggerGestureConst.Pointing_Upwards,
      SpellTriggerGestureConst.Leaning_Forwards_Upwards,
      SpellTriggerGestureConst.Horizontal,
      SpellTriggerGestureConst.Leaning_Forwards_Downwards,
      SpellTriggerGestureConst.Pointing_Downwards ]

    Fireball = Spell(name="Fireball", spell_trigger_actions=__triggers, spell_trigger_timeout=6)

