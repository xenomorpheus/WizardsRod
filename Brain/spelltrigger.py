class SpellTrigger():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def getName(self):
        return self.name
