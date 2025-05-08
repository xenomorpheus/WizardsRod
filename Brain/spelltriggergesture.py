from spelltrigger import SpellTrigger


class SpellTriggerGesture(SpellTrigger):

    def __init__(self, name):
        self.name = name

    def isTriggerdBy(self, event):
        return self.getName() == event.getTrigger().getName()
