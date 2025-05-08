from typing import List
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from staffeventbutton import StaffEventButton

'''
Created on 19 Sep. 2019

@author: bruins
'''


class ButtonEventGenerator(object):
    '''
    When hardware buttons are pressed send StaffEvent objects to
    listeners that have been previously setup.

    An example, each listener will be called with the following.

    listener.recieve_event(StaffEventButton(the_channel, now)

    '''

    def __init__(self, listeners, channels):
        '''
        Constructor
        '''
        self.channels = channels
        ''' a list of button integers for the buttons '''
        self.listeners = listeners
        ''' a list of objects that have the recieve_event method '''

    def activate(self):
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        for channel in self.channels:
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            # Set pin channel to be an input pin and set initial value to be
            # pulled low (off).
            # Setup event on pin channel rising edge. Ignore further edges for
            # 200ms for switch bounce handling.
            # Multiple callback handlers can be added
            GPIO.add_event_detect(channel, GPIO.RISING,
                                  callback=self._button_callback,
                                  bouncetime=200)

    def deactivate(self):
        for channel in self.channels:
            GPIO.remove_event_detect(channel)
            GPIO.cleanup()  # Clean up

    def _button_callback(self, the_channel):
        print("Button %d was pushed!" % (the_channel))
        now = 0 # TODO
        event = StaffEventButton(the_channel, now)
        for listener in self.listeners:
            listener.recieve_event(event)
