Overview:

This code is the orchestration of the wizards rod.  The wizards rod has a micro-controller running a 
bunch of sensors, emitters and other hardware.  The aim is when the rod is moved in certain ways, 
and/or buttons pressed, certain lights and other effects are triggered.


Exec Summary:

cd Brain
make


Concepts:

Keeping with the theme of a wizards rod, we introduce various concepts:

  spell - Is a definition of what rod effects we want to happen when a sequence of events are received in a particular time period.

  prepared spells - Any number of spells can be chosen to be prepared. A prepared spell is actively monitoring sensors on the rod looking
    for the particular sequence of events that trigger the spell. Once triggered the spell controls various actions on the rod.

  rod event - A hardware event on the rod e.g. button press, rod moved horizontal, GPS location reached, time reached, prox-card reader, etc.
       rod events are immutable.

  trigger - Code that recognises a rod event.
       triggers are immutable.

  trigger sequence - A sequence of trigger events to listen for.

  trigger time-out - The maximum time to wait for an entire trigger sequence.

  action - Some rod output e.g. flash lights, play sound, blutooth communication, etc.




Currently requires python 3.5 or greater

Development on non-pi environment
https://pypi.org/project/fake-rpigpio/
