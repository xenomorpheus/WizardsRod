""" hardware base class """


class Hardware():

    """ hardware base class. """

    def __init__(self, name: str, hardware_type='none') -> None:
        self.name = name
        self.hardware_type = hardware_type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hardware):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.hardware_type))

    def get_name(self) -> str:
        """ get the name """
        return self.name

    def get_hardware_type(self) -> str:
        """ get the hardware_type """
        return self.hardware_type

    def activate(self) -> None:
        """ make hardware available """

    def deactivate(self) -> None:
        """ finish using hardware """
