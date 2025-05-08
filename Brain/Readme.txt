
The smarts of the staff.

Let us think about it from the use case.  We are going to have a stream of Staff events flowing in, presumably from hardware.
We are going to need to know if we have performed the correct events to trigger a Spell.

My thoughts are as follows:

* We will have the concept of a spell - when certain staff events occur in sequence, an effect
    in generated.
* We will have a collection of spells which are known, but dormant.
* We have a set of "Prepared" spells, which we want to fire if certain staff movements (etc) are preformed.
* We have a stream of events, and new events are added to an end.
* We need to see if any of the prepared spells have been triggered.

I think something like.


    __fireball_triggers = [SpellTriggerGestureConst.Pointing_Upwards,
      SpellTriggerGestureConst.Leaning_Forwards_Upwards,
      SpellTriggerGestureConst.Horizontal,
      SpellTriggerGestureConst.Leaning_Forwards_Downwards,
      SpellTriggerGestureConst.Pointing_Downwards ]

    spell1 = Spell("Fireball").setTriggerActions(__fireball_triggers).setTriggerTimeout(6)
    spell2 = ...
    spell3 = ...

    # preparing a spell list
    prepared_spells = PreparedSpells('my prepared spell list')
    prepared_spells.spellAddList([spell1, spell2, spell3])
    prepared_spells.spellAdd(spell4)
    prepared_spells.spellDel('spell name')

    # Some spells might need special hardware, e.g. GPS
    hw_hints = prepared_spells.getHardwareHints()

    # looking for actions to trigger spells
    while True:
        new_action_list = getNewActions(hw_hints=hw_hints) # get new actions
        accepted_count = prepared_spells.acceptActions(new_action_list)
        if (accepted_count > 0):
            triggered_spells_list = prepared_spells.getTriggeredSpells()
            for spell in triggered_spells_list:
                # do spell stuff e.g. sound effects
                spell.performActions()



