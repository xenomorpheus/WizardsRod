class Staff():

    def __init__(self, name: str) -> None:
        self.name = name
        self.hardware_hints = []

    def getName(self) -> str:
        return self.name

    def setHardwareHints(self, hardware_hints) -> 'Staff':
        self.hardware_hints = hardware_hints
        return self

    def getNewStaffEvents(self):
        return[] # TODO
