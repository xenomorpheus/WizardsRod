
# Builder pattern


class Spell():

    def __init__(self, name):
        self.name = name
        # The actions required to trigger (activate) the spell
        self.trigger_actions = []
        # Maximum time to complete the spell
        self.trigger_timeout = 0
        # Some spells require hardware, e.g GPS, Accelerometer
        self.hardware_list = []

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.name

    def setTriggerActions(self, trigger_actions):
        self.trigger_actions = trigger_actions
        return self

    def getTriggerActions(self):
        return self.trigger_actions

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

