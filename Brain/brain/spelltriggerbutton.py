"""A spell trigger that looks for button press"""

from __future__ import absolute_import
from brain.spelltrigger import SpellTrigger


class SpellTriggerButton(SpellTrigger):
    """A spell trigger that looks for a specific button press"""

    def __init__(self, name) -> None:
        super().__init__(name, "BUTTON")
