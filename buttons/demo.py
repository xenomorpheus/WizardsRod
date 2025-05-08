import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library


def button_callback(channel):
    print("Button %d was pushed!" % (channel))


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
pin_num: int = 10
GPIO.setup(pin_num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin pin_num to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(pin_num, GPIO.RISING, callback=button_callback)  # Setup event on pin pin_num rising edge
message = input("Press enter to quit\n\n")  # Run until someone presses enter
GPIO.cleanup()  # Clean up
