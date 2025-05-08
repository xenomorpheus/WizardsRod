class Spell():

    def __init__(self, name, spell_trigger_actions, spell_trigger_timeout):
        self.name = name
        self.spell_trigger_actions = spell_trigger_actions
        self.spell_trigger_timeout = spell_trigger_timeout

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.name

    def getTriggerActions(self):
        return self.spell_trigger_actions

    def getTriggerTimeout(self):
        return self.spell_trigger_timeout
