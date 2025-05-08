
""" A sequence of spell triggers """

class SpellTriggerStream():

    """ A sequence of spell triggers """

#    def __init__(self):

    def __str__(self):
        return str(self.__dict__)

    def __eq_(self, other):
        return self.__dict__ == other.__dict__