from spelltrigger import SpellTrigger

class SpellTriggerGesture(SpellTrigger):

    def __init__(self, name, gesture):
        self.name = name
        self.gesture = gesture

    # Only the gesture matters, not the name
    def matchTrigger(self, other):
        return self.getGesture() == other.getGesture()

    def getGesture(self):
        return self.gesture
