"""

A set of Spells prepared and actively looking to be triggered by StaffEvent objects.


Builder pattern

"""

class SpellListPrepared():

    def __init__(self, name):
        self.name = name
        self.spell_trigger_event_timeout = 0
        self.spell_map = {}
        """ Prepared spells, keyed by spell name """
        self.spell_hardware = {}
        """ special hardware requirements. e.g. generate triggers """
        self.spell_triggers_permitted = {}
        """ Only the triggers of the prepared spells. keyed by trigger name """
        self.event_pending_list = []
        """ The events in the buffer.
        Only events that trigger prepared spells will be kept. """
        self.spell_trigger_sequence_all = {}
        """ Spells that have received some of the triggers  """
        self.__recalculate_spell_triggers()

    def __recalculate_spell_triggers(self):
        # work out what events could progress a prepared spell.
        # work out maximum time to wait for all triggers to receive events.
        self.spell_trigger_event_timeout = 0
        self.spell_triggers_permitted.clear()
        self.spell_hardware.clear()
        timeout_max = 0
        for spell_name, spell in self.spell_map.iteritems():
            timeout_max = max(timeout_max , spell.getTriggerTimeout())
            for spell_trigger in spell.getTriggerList():
                self.spell_triggers_permitted[spell_trigger.getName()] = spell_trigger
            for hardware in spell.getHardwareList():
                self.spell_hardware[hardware] = 1
        self.spell_trigger_event_timeout = timeout_max

    def getName(self):
        return self.name

    def spellAdd(self, spell):
        self.spell_map[spell.getName()] = spell
        self.__recalculate_spell_triggers()
        return self

    def spellAddList(self, spelllist):
        for spell in spelllist:
            self.spell_map[spell.getName()] = spell
        self.__recalculate_spell_triggers()
        return self

    def spellDel(self, spellName):
        if (self.spell_map.has_key(spellName)):
            del self.spell_map[spellName]
            self.__recalculate_spell_triggers()
        return self

    def acceptEvents(self, new_events):
        """
        accept events. Only keep the events that can trigger the prepared spells.
        returns a count of the number of events accepted. """
        count = 0
        for event in new_events:
            if any(trigger.isTriggerdBy(event) for trigger in self.spell_triggers_permitted.values()):
                self.event_pending_list.append(event)
                count += 1
        return count

    # consume staff events. Work out if any spells have hit all the triggers in sequence.
    # TODO not finished
    def getTriggeredSpells(self):
        triggered_spells_list = []
        spell_trigger_sequence_all = self.spell_trigger_sequence_all

        # consume staff events.
        event_pending_list = self.event_pending_list
        while(len(event_pending_list)):
            event = event_pending_list.pop(0)

            event_created_time = event.getCreated()
            for spell_name, sequence_list in spell_trigger_sequence_all.iteritems():
                spell = self.spell_map[spell_name]

                # Delete partially completed spell sequences if they timeout.
                sequence_list[:] = [sequence for sequence in sequence_list if event_created_time <= sequence["timeout"]]

                # If spell is waiting for that trigger next, then progress the spell to the next event or mark as complete.
                trigger_list = spell.getTriggerList()
                for sequence in sequence_list:
                    trigger_wanted_idx = sequence["trigger_wanted_idx"]
                    if (trigger_list[trigger_wanted_idx].isTriggerdBy(event)):
                        if ((len(trigger_list) - 1) < trigger_wanted_idx):
                            # progress to waiting for next event in trigger sequence
                            trigger_wanted_idx += 1
                        else:
                            # all triggers matched
                            sequence["timeout"] = 0  # TODO delete from trigger list
                            triggered_spells_list.append(spell)

            # If zeroth trigger, add the sequence to the list.
            for spell_name, spell in self.spell_map.iteritems():
                if (spell.getTriggerList()[0].isTriggerdBy(event)):
                    if (not spell_name in spell_trigger_sequence_all):
                        spell_trigger_sequence_all[spell_name] = []
                    spell_trigger_sequence_all[spell_name].append({ "trigger_wanted_idx" : 1, "timeout" : event_created_time + spell.getTriggerTimeout() })

        return triggered_spells_list

