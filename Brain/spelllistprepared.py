class SpellListPrepared():

    def __init__(self, name, spell_map):
        self.name = name
        self.spell_map = spell_map
        self.spell_trigger_action_timeout = 0
        self.spell_trigger_actions = {}
        self.__recalculate_spell_trigger_actions()

    def __recalculate_spell_trigger_actions(self):
        self.spell_trigger_actions_max = 0
        self.spell_trigger_actions.clear()
        actions_max = 0
        timeout_max = 0
        for spell_name, spell in self.spell_map.itervalues():
            actions_max = max(actions_max , len(spell.getTriggerActions()))
            timeout_max = max(timeout_max , spell.getTriggerTimeout())
            for spell_trigger_action in spell.getTriggerActions():
                self.spell_trigger_actions[spell_trigger_action + ''] = 1
        self.spell_trigger_actions_max = actions_max
        self.spell_trigger_action_timeout = timeout_max

    def getName(self):
        return self.name

    def spellAdd(self, spell):
        spell_map[spell.getName()] = spell
        self.__recalculate_spell_trigger_actions()

    def spellDel(self, spell):
        if (self.spell_map.has_key(spell.getName)):
            del spell_map[spell.getName()]
            self.__recalculate_spell_trigger_actions()

