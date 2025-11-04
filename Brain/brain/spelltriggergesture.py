"""A spell trigger that looks for rod movement"""

from __future__ import absolute_import
from brain.spelltrigger import SpellTrigger


class SpellTriggerGesture(SpellTrigger):
    """A spell trigger that looks for rod movement"""

    def __init__(self, name: str, gesture_type="GESTURE"):
        super().__init__(name, gesture_type)
