from spelltrigger import SpellTrigger


class SpellTriggerGesture(SpellTrigger):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.getName()

    def isTriggerdBy(self, event):
        return self.getName() == event.getTrigger().getName()
