
The smarts of the staff.

A framework to convert staff triggers into staff actions.


Somatic comparator returns false if not same class.

Otherwise return true IFF the direction component e.g. '442' is equal.

Let us think about it from the use case.  We are going to have a stream of Staff Actions flowing in.  We are going to need to know if we have met the requirements for a Spell.

My first thoughts are as follows.

We have a stream of actions, and new actions are added to an end.

We have a set of "Prepared" spells.

We need to see if any of the prepared spells have been triggered.

We also need to garbage collect, basically throw away useless actions.

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

    # looking for actions to trigger spells
    while(true) {
        new_action_list = ...# get new actions
        accepted_count = prepared_spells.acceptActions(new_action_list)
        if (accepted_count > 0):
            triggered_spells_list = prepared_spells.getTriggeredSpells()
            for spell in triggered_spells_list:
                # do spell stuff e.g. sound effects
    }


Notes about PreparedSpells class.
We need to throw away actions from the list because we need to keep the processing down, and we don't care about events that happened some time ago.

The PreparedSpells class could have the concept of:
a)  timeout (seconds) before an action expires (is removed from the list)

We just update this class variable when ever we add/remove spells to the prepared list.

There are trickier things to consider in the more general case, but we don't need to worry too much for now.
Consider the case where there is an action in the list that isn't related to any prepared spells.
The staff may still add the action to the list.  We may wish the prepared spell list to prune out actions that aren't components of the prepared spells.
Pretty easy to do, have a map of all actions for prepared spells. Refresh map when spells are added/removed.
Before looking for spells in the action list, remove actions we know we can ignore.

The downside of this approach is we may have a sequence of totally random actions, remove unwanted actions and somehow have a spell in the prepared list.
Perhaps the timeout will take care of that.
The think geek wizard robe solved this with a reset action (starting position "mana")
