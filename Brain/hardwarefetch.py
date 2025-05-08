'''
Created on 19 Sep. 2019

@author: bruins
'''

from hardware.buttoneventgenerator import ButtonEventGenerator


class HardwareFetch():
    '''
    HardwareFetch
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def get(self, hint: str):
        ''' return hardware object using hint as selector '''
        if hint == 'button':
            return ButtonEventGenerator()
        raise Exception("Hint "+hint+" not known")
