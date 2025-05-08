'''
Created on 19 Sep. 2019

@author: bruins
'''

from buttoneventgenerator import ButtonEventGenerator


class HardwareFetch():
    '''
    HardwareFetch
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.beg = ButtonEventGenerator()

    def __str__(self):
        return self.__class__.__name__

    def get(self, hint: str):
        ''' return hardware object using hint as selector '''
        if hint == 'BUTTON':
            return self.beg
        raise Exception("Hint "+hint+" not known")
