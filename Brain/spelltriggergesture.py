from spelltrigger import SpellTrigger

class SpellTriggerGesture(SpellTrigger):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.getName()

    # Only the gesture matters, not the name
    def matchTrigger(self, other):
        return self.getName() == other.getName()

