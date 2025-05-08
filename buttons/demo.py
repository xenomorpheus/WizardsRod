#!/usr/bin/env python3

# Import Raspberry Pi GPIO library
try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()

def button_callback(the_channel: int):
    print("Button %d was pushed!" % (the_channel))


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
channel: int = 10
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Set pin channel to be an input pin and set initial value to be pulled low
#    (off).
# Setup event on pin channel rising edge. Ignore further edges for 200ms for
#    switch bounce handling
# Multiple callback handlers can be added

GPIO.add_event_detect(channel, GPIO.RISING, callback=button_callback,
                      bouncetime=200)
message = input("Press enter to quit\n\n")  # Run until someone presses enter
GPIO.remove_event_detect(channel)
GPIO.cleanup()  # Clean up
