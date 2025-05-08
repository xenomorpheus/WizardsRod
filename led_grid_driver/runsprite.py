#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
from hal9000 import Hal9000
from knightrider import KnightRider
from sprite import Sprite

X_SIZE = 3
Y_SIZE = 100
NUM_LED = X_SIZE * Y_SIZE

print ('Sprite')

MY_CYCLE = Sprite(num_led=NUM_LED, pause_value=1.000,
                       num_steps_per_cycle=1, num_cycles=1,
                       global_brightness=100)
MY_CYCLE.set_x(X_SIZE)
MY_CYCLE.set_y(Y_SIZE)
SPRITE_FILENAME = 'sprite/test pattern 3x100_1.png'  # image can be in gif jpeg or png format 
MY_CYCLE.set_pix(SPRITE_FILENAME)


for i in range(3):
   MY_CYCLE.start()

print ('Finished the test')
