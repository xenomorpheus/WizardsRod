
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


spell1 = Spell(name="Fireball", components=( Somatic(442, 'Pointing Upwards'), Somatic(424, Horizonta'),...))
spell2 = ...
spell3 = ...

# preparing a spell list
prepared_spells = PreparedSpells(spell_list=(spell1, spell2, spell3))
prepared_spells.add(spell4)
prepared_spells.remove(name='spell name')

# looking for actions to trigger spells
while(true) {
    action_list.append_actions()
    triggered_spells_list = prepared_spells.process_actions(actions=action_list)
    # do spell stuff e.g. sound effects
}


Notes about PreparedSpells class.
We need to throw away actions from the list because we need to keep the processing down, and we don't care about events that happened some time ago.

The PreparedSpells class could have the concept of:
a)  timeout (seconds) before an action expires (is removed from the list)
b)  action_count_max  - maximum number of actions to keep in the list.

We can easily calculate action_count_max, it is the spell with the largest number of components
We just update this class variable when ever we add/remove spells to the prepared list.

There are trickier things to consider in the more general case, but we don't need to worry too much for now.
Consider the case where there is an action in the list that isn't related to any prepared spells.
The staff may still add the action to the list.  We may wish the prepared spell list to prune out actions that aren't components of the prepared spells.
Pretty easy to do, have a map of all actions for prepared spells. Refresh map when spells are added/removed.
Before looking for spells in the action list, remove actions we know we can ignore.

The downside of this approach is we may have a sequence of totally random actions, remove unwanted actions and somehow have a spell in the prepared list.
Perhaps the timeout will take care of that.
The think geek wizard robe solved this with a reset action (starting position "mana")
