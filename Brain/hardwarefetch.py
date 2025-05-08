'''
Created on 19 Sep. 2019

@author: bruins
'''

from hardware.buttoneventgenerator import ButtonEventGenerator

class HardwareFetch(object):
    '''
    HardwareFetch
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def get(self, hint: str):
        if str == 'button':
            return ButtonEventGenerator()
        return
