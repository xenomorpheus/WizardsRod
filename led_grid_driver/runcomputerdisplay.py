#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
from hal9000 import Hal9000
from knightrider import KnightRider

#NUM_LED = 430
X_SIZE = 3
Y_SIZE = 100
NUM_LED = X_SIZE * Y_SIZE


print('HAL9000')
MY_CYCLE = Hal9000(num_led = NUM_LED, pause_value=4,
                               num_cycles=1, global_brightness=10)
MY_CYCLE.set_x(X_SIZE)
MY_CYCLE.set_y(Y_SIZE)
MY_CYCLE.start()

print('KnightRider')
MY_CYCLE = KnightRider(num_led=NUM_LED, pause_value=0.02,
                               num_steps_per_cycle=170, num_cycles=2,
                               global_brightness=20)
MY_CYCLE.set_x(X_SIZE)
MY_CYCLE.set_y(Y_SIZE)
MY_CYCLE.start()

print('Finished the test')
