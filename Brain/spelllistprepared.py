# Builder pattern


class SpellListPrepared():

    def __init__(self, name):
        self.name = name
        self.spell_trigger_event_timeout = 0
        # Prepared spells, keyed by spell name
        self.spell_map = {}
        # special hardware requirements
        self.spell_hardware = {}
        # The trigger of the prepared spells, keyed by trigger name
        self.spell_triggers_permitted = {}
        # The events in the buffer.
        # Only events that trigger prepared spells will be kept.
        self.event_pending_list = []
        # Spells that have received some of the triggers
        self.spell_trigger_list_by_spell_name_map = {}
        self.__recalculate_spell_triggers()

    # work out what events could progress a prepared spell
    # work out maximum time to wait for all triggers to receive events
    def __recalculate_spell_triggers(self):
        self.spell_trigger_event_timeout = 0
        self.spell_triggers_permitted.clear()
        self.spell_hardware.clear()
        timeout_max = 0
        for spell_name, spell in self.spell_map.iteritems():
            timeout_max = max(timeout_max , spell.getTriggerTimeout())
            for spell_trigger in spell.getTriggerList():
                self.spell_triggers_permitted[spell_trigger.getName()] = 1
            for hardware in spell.getHardwareList():
                self.spell_hardware[hardware] = 1
        self.spell_trigger_event_timeout = timeout_max

    def getName(self):
        return self.name

    def spellAdd(self, spell):
        self.spell_map[spell.getName()] = spell
        self.__recalculate_spell_triggers()
        return self

    def spellAddList(self, list):
        for spell in list:
            self.spell_map[spell.getName()] = spell
        self.__recalculate_spell_triggers()
        return self

    def spellDel(self, spellName):
        if (self.spell_map.has_key(spellName)):
            del self.spell_map[spell.spellName]
            self.__recalculate_spell_triggers()
        return self

    # accept events. Only keep the events that can trigger the prepared spells
    # returns a count of the number of events accepted
    def acceptEvents(self, new_events):
        count = 0
        for event in new_events:
            if (self.spell_triggers_permitted.has_key(event.getName())):
                self.event_pending_list.append(event)
                count += 1
        return count

    # consume spell triggers. Work out if any spells have hit all the triggers in sequence
    def getTriggeredSpells(self):
        triggered_spells_list = []
        spell_trigger_list_by_spell_name_map = self.spell_trigger_list_by_spell_name_map

        # consume spell triggers.
        event_pending_list = self.event_pending_list
        while(len(event_pending_list)):
            event = event_pending_list.pop(0)

            # Cancel partially completed spells if they timeout.
            trigger_created_time = event.getCreated()
            for spell_name, spell_trigger_list in spell_trigger_list_by_spell_name_map.iteritems():
                spell_trigger_list[:] = [trigger for trigger in spell_trigger_list if trigger.timeout < trigger_created_time]

            # if spell is waiting for that trigger next, then progress the spell to the next symbol or mark as complete.
            # TODO for spell_name, spell_trigger_list in spell_trigger_list_by_spell_name_map.iteritems():

            # Next add any spells to the map

        return triggered_spells_list  # TODO not finished

