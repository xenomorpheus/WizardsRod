

'''
An event that occurs on the staff.  Spells will be triggered by a sequence of these events.

* A button is pressed.
* A gesture/stamp of the staff
* A temperature change
* A pressure change
* Reaching a GPS location

'''


class StaffEvent():

    def __init__(self, name, trigger, created):
        self.name = name
        self.trigger = trigger
        self.created = created

    def __str__(self):
        return self.getName()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    def getName(self):
        return self.name

    def getTrigger(self):
        return self.trigger
    
    def getCreated(self):
        return self.created

