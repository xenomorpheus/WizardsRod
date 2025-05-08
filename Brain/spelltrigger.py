class SpellTrigger():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.getName())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def getName(self):
        return self.name
