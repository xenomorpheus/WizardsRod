class SpellTrigger():

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def getName(self):
        return self.name

    def isTriggerdBy(self, event):
        """ For simple triggers, the event name just has to match. """
        return self.getName() == event.getName()
