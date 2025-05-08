
# Builder pattern


class SpellListPrepared():

    def __init__(self, name):
        self.name = name
        self.spell_trigger_action_timeout = 0
        # Prepared spells, keyed by spell name
        self.spell_map = {}
        # The trigger actions of the prepared spells, keyed by trigger action name
        self.spell_trigger_actions = {}
        # The actions in the buffer.
        # Only actions that trigger prepared spells will be kept.
        self.action_list = []
        self.__recalculate_spell_trigger_actions()

    def __recalculate_spell_trigger_actions(self):
        self.spell_trigger_actions_max = 0
        self.spell_trigger_actions.clear()
        timeout_max = 0
        for spell_name, spell in self.spell_map.iteritems():
            timeout_max = max(timeout_max , spell.getTriggerTimeout())
            for spell_trigger_action in spell.getTriggerActions():
                self.spell_trigger_actions[spell_trigger_action.getName()] = 1
        self.spell_trigger_action_timeout = timeout_max

    def getName(self):
        return self.name

    def spellAdd(self, spell):
        self.spell_map[spell.getName()] = spell
        self.__recalculate_spell_trigger_actions()
        return self

    def spellAddList(self, list):
        for spell in list:
            self.spell_map[spell.getName()] = spell
        self.__recalculate_spell_trigger_actions()
        return self

    def spellDel(self, spellName):
        if (self.spell_map.has_key(spellName)):
            del self.spell_map[spell.spellName]
            self.__recalculate_spell_trigger_actions()
        return self

    # accept actions. Only keep the actions that can trigger the prepared spells
    # returns a count of the number of actions accepted
    def acceptActions(self, new_actions):
        count = 0
        for action in new_actions:
            if (self.spell_trigger_actions.has_key(action.getName())):
                self.action_list.append(action)
                count+=1
        return count

    def getTriggeredSpells(self):
        triggered_spells_list = []
        return triggered_spells_list  # TODO not finished

