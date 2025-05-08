
""" A spell trigger that looks for movement """

from __future__ import absolute_import
from spelltrigger import SpellTrigger


class SpellTriggerButton(SpellTrigger):

    """ A spell trigger that looks for button press """

    def __init__(self, name: str, type='BUTTON') -> None:
        SpellTrigger.__init__(self, name, type)
