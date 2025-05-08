#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip.


PYTHONPATH=./APA102_Pi:. ./spriteplayer_demo.py --sprite=sprite/lightningX_30x100.png 



"""
import sys
import argparse
from spriteplayer import SpritePlayer


class SpritePlayerDemo:

    def spriteplayer_demo(sprite_filename, x_size=3, y_size=100):
        num_led = x_size * y_size

        print ('Sprite')

        spriteplayer = SpritePlayer(num_led=num_led, pause_value=9.050,
                               num_steps_per_cycle=1, num_cycles=1, # 10
                               global_brightness=2)
        spriteplayer.set_x(x_size)
        spriteplayer.set_y(y_size)
        spriteplayer.set_sprite_filename(sprite_filename)
        spriteplayer.start()

        print ('Finished the test')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    #parser.add_argument(
    #    "--mode",
    #    type=str,
    #    default="hsv",
    #    help="Mode (hsv, lab)")
    #parser.add_argument(
    #    "--save-dir",
    #    type=str,
    #    help="Save results to dir")
    parser.add_argument(
        "--sprite",
        type=str,
        default=None,
        help="filename of sprite to show")
    #parser.add_argument(
    #    "--batch",
    #    action="store_true",
    #    help="Run in batch mode, skipping wait for key",
    #    default=False)

    args = parser.parse_args()
    sprite_filename = args.sprite

    SpritePlayerDemo.spriteplayer_demo(sprite_filename=sprite_filename)
