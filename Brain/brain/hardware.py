""" hardware base class """


class Hardware():

    """ hardware base class. """

    def __init__(self, name: str, type='none') -> None:
        self.name = name
        self.type = type

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hardware):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.type))

    def get_name(self) -> str:
        """ get the name """
        return self.name

    def get_type(self) -> str:
        """ get the type """
        return self.type

    def activate(self) -> None:
        """ make hardware available """
        pass

    def deactivate(self) -> None:
        """ finish using hardware """
        pass
