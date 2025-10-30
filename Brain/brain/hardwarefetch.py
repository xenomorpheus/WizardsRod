"""
Used to fetch hardware interfaces using hardware hints.

e.g. "BUTTON" for button event generator hardware.

"""

from typing import Dict
from brain.hardware import Hardware
from brain.buttoneventgenerator import ButtonEventGenerator


class HardwareFetch:
    """
    HardwareFetch
    """

    generator = {}  # type: Dict[str, Hardware]

    def __init__(self):
        """
        Constructor
        """
        self.generator["BUTTON"] = ButtonEventGenerator()

    def __str__(self):
        return self.__class__.__name__

    def get(self, hint: str) -> Hardware:
        """return hardware object using hint as selector"""
        if hint in self.generator:
            return self.generator[hint]
        raise IOError("Hint " + hint + " not known")
