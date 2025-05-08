This code is the orchestration of the wizards staff.  The wizards staff has a micro-controller running a bunch of sensors, emitters and other hardware.  The aim is when the staff is moved in certain ways, and/or buttons pressed, certain lights and other effects are triggered.

Keeping with the theme of a wizards staff, we introduce various concepts:

  spell - Is a definition of what staff effects we want to happen when a sequence of events are received in a particular time period.

  prepared spells - Any number of spells can be chosen to be prepared. A prepared spell is actively monitoring sensors on the staff looking
    for the particular sequence of events that trigger the spell. Once triggered the spell controls various actions on the staff.

  staff event - A hardware event on the staff e.g. button press, staff moved horizontal, GPS location reached, time reached, prox-card reader, etc.
       staff events are immutable.

  trigger - Code that recognises a staff event.
       triggers are immutable.

  trigger sequence - A sequence of trigger events to listen for.

  trigger time-out - The maximum time to wait for an entire trigger sequence.

  action - Some staff output e.g. flash lights, play sound, blutooth communication, etc.




Currently requires python 3.5 or greater

sudo apt install python3-pip

# Unit testing in Python 3
python3 -m pip install pytest
python3 -m pip install coverage

# Python style checking
python3 -m pip install pylint --user
python3 -m pip install mypy --user
python3 -m pip install pycodestyle --user

# TODO
# Was I using pydoc previously?
# python3 -m pip install pydoc --user
# python3 -m pip install pdoc3 --user
