"""
A specific Spell's definition.

Builder pattern.

"""

class Spell():


    def __init__(self, name):
        self.name = name
        """ Name of the spell """
        self.trigger_list = []
        """ Ordered steps required to trigger the spell """
        self.trigger_timeout = 0
        """ Maximum time to complete the spell. """
        self.hardware_list = []
        """ Some spells are triggered by hardware actions. e.g Buttons, GPS, Accelerometer """

    def getName(self):
        return self.name

    def setTriggerList(self, trigger_list):
        self.trigger_list = trigger_list
        return self

    def getTriggerList(self):
        return self.trigger_list

    def setTriggerTimeout(self, trigger_timeout):
        self.trigger_timeout = trigger_timeout
        return self

    def getTriggerTimeout(self):
        return self.trigger_timeout

    def setHardwareList(self, hardware_list):
        self.hardware_list = hardware_list
        return self

    def getHardwareList(self):
        return self.hardware_list

