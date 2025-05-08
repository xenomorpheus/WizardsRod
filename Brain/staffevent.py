

"""
An event that occurs on the staff.  Spells will be triggered by a sequence of these events.

* A button is pressed.
* A gesture/stamp of the staff
* A temperature change
* A pressure change
* Reaching a GPS location

"""


class StaffEvent():

    def __init__(self, name, created):
        self.name = name
        self.created = created

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.created))

    def getName(self):
        return self.name
    
    def getCreated(self):
        return self.created

