"""
HardwareFetch
"""

from typing import Dict
from brain.hardware import Hardware
from brain.buttoneventgenerator import ButtonEventGenerator


class HardwareFetch:
    """
    HardwareFetch

    Used to fetch hardware interfaces using hardware hints.

    e.g. "BUTTON" for button event generator hardware.

    Example usage:
    hardware_hint = "BUTTON"
    hardware = hwf.get(hardware_hint)

    """

    generator = {}  # type: Dict[str, Hardware]

    def __init__(self):
        """
        Constructor
        """
        self.generator["BUTTON"] = ButtonEventGenerator()
        """ map of hardware hint to hardware object """

    def get(self, hint: str) -> Hardware:
        """return hardware object using hint as selector"""
        if hint in self.generator:
            return self.generator[hint]
        raise IOError("Hardware generator not known for Hint: " + hint)

    def set(self, hint: str, hardware: Hardware) -> None:
        """set hardware object for hint"""
        self.generator[hint] = hardware
