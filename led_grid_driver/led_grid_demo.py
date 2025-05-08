#!/usr/bin/env python3
"""

Sample script to run a few colour tests on the strip.

PYTHONPATH=./APA102_Pi:. ./led_grid_driver_demo.py

1. HAL9000 text and red eye shown as a a static display.
2. Knightrider red eye bounces backwards and forwards.


"""
from hal9000 import Hal9000
from knightrider import KnightRider

#NUM_LED = 430
X_SIZE = 3
Y_SIZE = 100
NUM_LED = X_SIZE * Y_SIZE


print ('HAL9000')
MY_CYCLE = Hal9000(num_led=NUM_LED, pause_value=0.1, num_cycles=1,
                   global_brightness=40)
MY_CYCLE.set_x(X_SIZE)
MY_CYCLE.set_y(Y_SIZE)
MY_CYCLE.start()

print ('KnightRider')
MY_CYCLE = KnightRider(num_led=NUM_LED, pause_value=0.000,
                       num_steps_per_cycle=100, num_cycles=4,
                       global_brightness=40)
MY_CYCLE.set_x(X_SIZE)
MY_CYCLE.set_y(Y_SIZE)
MY_CYCLE.start()

#print ('Sprite')
#MY_CYCLE = Sprite(num_led=NUM_LED, pause_value=0.0000,
#                       num_steps_per_cycle=1, num_cycles=10,
#                       global_brightness=80)
#MY_CYCLE.set_x(X_SIZE)
#MY_CYCLE.set_y(Y_SIZE)
#MY_CYCLE.start()

print ('Finished the test')
