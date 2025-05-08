
""" A spell trigger that looks for movement """

from __future__ import absolute_import
from spelltriggertype import SpellTriggerType


class SpellTriggerTypeGesture(SpellTriggerType):

    """ A spell trigger that looks for movement """

    def __init__(self, name: str) -> None:
        SpellTriggerType.__init__(self, name)
