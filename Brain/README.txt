Overview:

This code is the orchestration of the wizards rod.  The wizards rod has a micro-controller running a 
bunch of sensors, emitters and other hardware.  The aim is when the rod is moved in certain ways, 
and/or buttons pressed, certain lights and other effects are triggered.


Exec Summary:

cd Brain
make


Concepts:

Keeping with the theme of a wizards rod, we introduce various concepts:

  Rod - has a Spell List Prepared. 
        A rod also maintains a set of active hardware drivers needed by the current set of prepared spells.

  Spell - Is a definition of a Trigger Sequence to be received, within in a trigger time-out period, then what Actions perform.

  Spell List Prepared - A set of Spells that are actively looking for Rod Events to complete their Trigger Sequences.
     A Spell List Prepared knows the hardware required to generate events of all of the Spells.
     As Rod Events are received the Spell List Prepared will track the Trigger Sequences of each spell, and if 
     a Triggger Sequence completes, run the Spell's Action.

  Rod Event - A hardware event on the rod e.g. button press, rod moved horizontal, GPS location reached, time reached, prox-card reader, etc.
       Rod Events are used by Spell Triggers.
       Rod Events are immutable.

  Spell Trigger - Code that recognises a Rod Event.
       Spell Triggers are immutable.
       Spell Triggers have a type which is a hint to what hardware driver is needed to generate that type of Rod Event.

  Trigger Sequence - A sequence of Spell Triggers.

  trigger time-out - The maximum time to wait for an entire trigger sequence.

  Action - Some rod output e.g. flash lights, play sound, blutooth communication, etc.




Currently requires python 3.5 or greater

Development on non-pi environment
https://pypi.org/project/fake-rpigpio/
