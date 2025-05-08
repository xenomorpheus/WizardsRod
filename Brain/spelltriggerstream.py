class SpellTriggerStream():

#    def __init__(self):


    def __str__(self):
        return str(self.__dict__)

    def __cmp__(self, other): 
        return self.__dict__ == other.__dict__

