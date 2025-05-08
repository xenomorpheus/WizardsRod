""" A Spell has a sequence of triggers that need to be satisfied.
Each trigger has a type.  """

from __future__ import absolute_import


class SpellTriggerType():

    """ A Spell has a sequence of triggers that need to be satisfied.
    Each trigger has a type.  """
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __key(self) -> str:
        return self.name

    def __eq__(self, other: 'SpellTriggerType'):
        return (type(self) is type(other)) and (self.get_name() == other.get_name())

    def __hash__(self):
        return hash(self.__key())

    def get_name(self) -> str:
        """ get the name """
        return self.name
