"""A spell trigger that looks for movement"""

from __future__ import absolute_import
from spelltrigger import SpellTrigger


class SpellTriggerGesture(SpellTrigger):
    """A spell trigger that looks for movement"""

    def __init__(self, name: str, gesture_type="GESTURE"):
        super().__init__(name, gesture_type)
