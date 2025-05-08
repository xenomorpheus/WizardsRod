This code is the orchestration of the wizards staff.  The wizards staff has a micro-controller running a bunch of sensors, emitters and other hardware.  The aim is when the staff is moved in certain ways, and/or buttons pressed, certain lights and other effects are triggered.

Keeping with the theme of a wizards staff, we introduce various concepts:

  spell - Is a definition of what staff effects we want to happen when a sequence of events are received in a particular time period.

  prepared spells - Only prepared spells look for staff events and perform staff effects. That way we can choose the sub-set of spells that are active at given time.

  staff event - A hardware event on the staff e.g. button press, staff moved horizontal, GPS location reached, time reached, prox-card reader, etc.

  trigger - Code that recognises a staff event.

  trigger sequence - A sequence of trigger events to listen for.

  trigger time-out - The maximum time to wait for an entire trigger sequence.

  action - Some staff output e.g. flash lights, play sound, blutooth communication, etc.





