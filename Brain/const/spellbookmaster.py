from spell import Spell
from const.spelltriggergestureconst import SpellTriggerGestureConst as gesture
from const.spellhardwareconst import SpellHardwareConst as hw

class SpellBookMaster():

    __fireball_triggers = [gesture.Pointing_Upwards,
      gesture.Leaning_Forwards_Upwards,
      gesture.Horizontal,
      gesture.Leaning_Forwards_Downwards,
      gesture.Pointing_Downwards ]

    Fireball = Spell("Fireball").setTriggerActions(__fireball_triggers).setTriggerTimeout(6) \
        .setHardwareList([hw.ACCELEROMETER])
