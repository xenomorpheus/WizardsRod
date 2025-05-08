
     Wizard's Staff

A collection of drivers for equipment connected to a Raspberry Pi.

The long term aim is to make a fun project styled on a wizard's staff.


Developer
==============

Suggestion is to use virtualenv to manage project environment and dependencies

    https://realpython.com/python-virtual-environments-a-primer/
    python3 -m venv  ~/Desktop/staff/env      # Create environment
    source ~/Desktop/staff/env/bin/activate   # Activate (start using) the enviroment
    pip3 install RPi.GPIO                     # Install packages
    pip3 freeze > requirements.txt            # Update the required list of packages
