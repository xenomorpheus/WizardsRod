
# Builder pattern

class Spell():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.name

    def setTriggerActions(self, spell_trigger_actions):
        self.spell_trigger_actions = spell_trigger_actions
        return self

    def getTriggerActions(self):
        return self.spell_trigger_actions

    def setTriggerTimeout(self, spell_trigger_timeout):
        self.spell_trigger_timeout = spell_trigger_timeout
        return self

    def getTriggerTimeout(self):
        return self.spell_trigger_timeout
