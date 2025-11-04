"""A spell trigger that looks for movement"""

from __future__ import absolute_import
from brain.spelltrigger import SpellTrigger


class SpellTriggerButton(SpellTrigger):
    """A spell trigger that looks for button press"""

    def __init__(self, name: str, trigger_type="BUTTON") -> None:
        SpellTrigger.__init__(self, name, trigger_type)
