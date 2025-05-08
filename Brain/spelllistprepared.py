# Builder pattern


class SpellListPrepared():

    def __init__(self, name):
        self.name = name
        self.spell_trigger_event_timeout = 0
        # Prepared spells, keyed by spell name
        self.spell_map = {}
        # special hardware requirements
        self.spell_hardware = {}
        # Only the triggers of the prepared spells. keyed by trigger name
        self.spell_triggers_permitted = {}
        # The events in the buffer.
        # Only events that trigger prepared spells will be kept.
        self.event_pending_list = []
        # Spells that have received some of the triggers
        self.spell_trigger_sequence_all = {}
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

    # consume spell triggers. Work out if any spells have hit all the triggers in sequence.
    # TODO not finished
    def getTriggeredSpells(self):
        triggered_spells_list = []
        spell_trigger_sequence_all = self.spell_trigger_sequence_all

        # consume spell triggers.
        event_pending_list = self.event_pending_list
        while(len(event_pending_list)):
            event = event_pending_list.pop(0)
            print "Saw event:" + event.getName()

            event_created_time = event.getCreated()
            for spell_name, sequence_list in spell_trigger_sequence_all.iteritems():
                spell = self.spell_map[spell_name]

                # Delete partially completed spell sequences if they timeout.
                sequence_list[:] = [sequence for sequence in sequence_list if event_created_time <= sequence["timeout"]]

                # If spell is waiting for that trigger next, then progress the spell to the next event or mark as complete.
                for sequence in sequence_list:
                    trigger_list = spell.getTriggerList()
                    if (trigger_list[sequence["trigger_wanted"]].getName() == event.getEvent().getName()):
                        if ((len(trigger_list) - 1) < sequence["trigger_wanted"]):
                            # progress to waiting for next event in trigger sequence
                            sequence["trigger_wanted"] += 1
                        else:
                            # all triggers matched
                            sequence["timeout"] = 0  # TODO delete from trigger list
                            triggered_spells_list.append(spell)

            # If zeroth trigger, add the sequence to the list.
            for spell_name, spell in self.spell_map.iteritems():
                if (spell.getTriggerList()[0].getName() == event.getEvent().getName()):
                    if (not spell_name in spell_trigger_sequence_all):
                        spell_trigger_sequence_all[spell_name] = []
                    spell_trigger_sequence_all[spell_name].append({ "trigger_wanted" : 1, "timeout" : event_created_time + spell.getTriggerTimeout() })

        return triggered_spells_list

