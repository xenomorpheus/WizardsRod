"""
Created on 19 Sep. 2019

@author: bruins
"""

from typing import Dict
from hardware import Hardware
from buttoneventgenerator import ButtonEventGenerator


class HardwareFetch():
    """
    HardwareFetch
    """
    generator = {}  # type: Dict[str, Hardware]

    def __init__(self):
        """
        Constructor
        """
        self.generator['BUTTON'] = ButtonEventGenerator()

    def __str__(self):
        return self.__class__.__name__

    def get(self, hint: str) -> Hardware:
        """ return hardware object using hint as selector """
        if hint in self.generator:
            return self.generator[hint]
        raise Exception("Hint "+hint+" not known")
