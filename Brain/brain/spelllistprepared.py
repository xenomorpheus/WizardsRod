"""

A set of Spells prepared and actively looking to be triggered by RodEvent
objects.


"""

from typing import Any, Dict, List, Set
from brain.spell import Spell
from brain.rodevent import RodEvent
from brain.spelltrigger import SpellTrigger


class SpellListPrepared:
    """

    Builder pattern

    Notes

    We need to throw away actions from the list because we need to keep the
    processing down, and we don't care about events that happened some time ago.

    The class could have the concept of:
    a)  timeout (seconds) before an action expires (is removed from the list)

    We just update this class variable when ever we add/remove spells to the
    prepared list.

    There are trickier things to consider in the more general case, but we don't
    need to worry too much for now.

    Consider the case where there is an action in the list that isn't related to
    any prepared spells.

    The rod may still add the action to the list.  We may wish the prepared spell
    list to prune out actions that aren't components of the prepared spells.

    Pretty easy to do, have a map of all actions for prepared spells. Refresh map
    when spells are added/removed.
    Before looking for spells in the action list, remove actions we know we can
    ignore.

    The down-side of this approach is we may have a sequence of totally random
    actions, remove unwanted actions and somehow have a spell in the prepared list.
    Perhaps the timeout will take care of that.

    The Thinkgeek wizard robe solved this with a reset action (starting position
    "mana")

    """

    def __init__(self) -> None:
        self.spell_trigger_event_timeout = 0
        self.spell_list = []  # type: List[Spell]
        """ Prepared spells, keyed by spell name """
        self.hardware_hints = set()  # type: Set[str]
        """ special hardware requirements. e.g. generate triggers """
        self.spell_triggers_permitted = set()  # type: Set[SpellTrigger]
        """ Only the triggers of the prepared spells. keyed by trigger name """
        self.event_pending_list = []  # type: List[RodEvent]
        """ The events in the buffer.
        Only events that trigger prepared spells will be kept. """
        self.spell_trigger_sequence_all = {}  # type: Dict[Spell, List[Dict[str, Any]]]
        """ For each prepared spell, a sequence of indexes to that spell's
        triggers. Each spell trigger sequence may have repeats of triggers.
        Analogy: entering a numeric security code needs to support
        repeats of digits.   """
        self.__recalculate_spell_triggers()

    def __recalculate_spell_triggers(self) -> None:
        # work out what events could progress a prepared spell.
        # work out maximum time to wait for all triggers to receive events.
        # Update the list of hardware we are monitoring.
        self.spell_trigger_event_timeout = 0
        self.spell_triggers_permitted.clear()
        self.hardware_hints.clear()
        timeout_max = 0
        for spell in self.spell_list:
            timeout_max = max(timeout_max, spell.get_trigger_timeout())
            for trigger in spell.get_trigger_sequence():
                self.spell_triggers_permitted.add(trigger)
                self.hardware_hints.add(trigger.get_trigger_type())
        self.spell_trigger_event_timeout = timeout_max

    def get_hardware_hints(self) -> set:
        """get the hardware hints"""
        return self.hardware_hints

    def spell_add(self, spell: Spell) -> "SpellListPrepared":
        """add a spell to the list of prepared spells. This will
        automatically handle connections to any required hardware."""
        self.spell_list.append(spell)
        self.__recalculate_spell_triggers()
        return self

    def spell_add_list(self, spell_list: List[Spell]) -> "SpellListPrepared":
        """add a list of spells"""
        # TODO check spell has triggers
        for spell in spell_list:
            self.spell_list.append(spell)
        self.__recalculate_spell_triggers()
        return self

    def spell_del(self, spell: Spell) -> "SpellListPrepared":
        """remove a spell"""
        if spell in self.spell_list:
            self.spell_list.remove(spell)
            self.__recalculate_spell_triggers()
        return self

    def receive_events(self, new_events: List[RodEvent]) -> List[Spell]:
        """accept events"""
        spells_triggered = []  # type: List[Spell]
        for event in new_events:
            for spell in self.receive_event(event):
                spells_triggered.append(spell)
        return spells_triggered

    def receive_event(self, event: RodEvent) -> List[Spell]:
        """Consume rod events. Determine which spells, if any, have had all
        triggers in sequence, and within the timeout period.
        """
        spells_triggered = []  # type: List[Spell]
        if not any(trigger.is_triggerd_by(event) for trigger in self.spell_triggers_permitted):
            return spells_triggered
        event_created_time = event.get_created()
        for spell, sequence_list in self.spell_trigger_sequence_all.items():

            # Delete partially completed spell sequences if they have timed out.
            sequence_list[:] = [sequence for sequence in sequence_list if event_created_time <= sequence["timeout"]]

            # If spell is waiting for that trigger next, then progress the spell to the next event or mark as complete.
            trigger_list = spell.get_trigger_sequence()
            for sequence in sequence_list:
                trigger_wanted_idx = sequence["trigger_wanted_idx"]
                if trigger_list[trigger_wanted_idx].is_triggerd_by(event):
                    if (len(trigger_list) - 1) < trigger_wanted_idx:
                        # progress to waiting for next event in trigger sequence
                        trigger_wanted_idx += 1
                    else:
                        # all triggers matched
                        sequence["timeout"] = 0
                        # TODO delete from list
                        spells_triggered.append(spell)

        # If zeroth trigger, add the sequence to the list.
        for spell in self.spell_list:
            if len(spell.get_trigger_sequence()) > 0 and spell.get_trigger_sequence()[0].is_triggerd_by(event):
                if spell not in self.spell_trigger_sequence_all:
                    self.spell_trigger_sequence_all[spell] = []
                self.spell_trigger_sequence_all[spell].append(
                    {"trigger_wanted_idx": 1, "timeout": event_created_time + spell.get_trigger_timeout()}
                )

        return spells_triggered
