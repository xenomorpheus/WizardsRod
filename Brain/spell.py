"""
A specific Spell's definition.

Builder pattern.

"""

class Spell():


    def __init__(self, name: str):
        self.name = name
        """ Name of the spell """
        self.trigger_sequence = []
        """ Ordered steps required to trigger the spell """
        self.trigger_timeout = 0
        """ Maximum time to complete the spell. """
        self.hardware_set = []
        """ Some spells are triggered by hardware actions. e.g Buttons, GPS, Accelerometer """

    def getName(self):
        return self.name

    def setTriggerSequence(self, trigger_sequence):
        self.trigger_sequence = trigger_sequence
        return self

    def getTriggerSequence(self):
        return self.trigger_sequence

    def setTriggerTimeout(self, trigger_timeout):
        self.trigger_timeout = trigger_timeout
        return self

    def getTriggerTimeout(self):
        return self.trigger_timeout

    def setHardwareSet(self, hardware_set):
        self.hardware_set = hardware_set
        return self

    def getHardwareSet(self):
        return self.hardware_set

    def performActionns(self):
        # TODO stuff
        return self

