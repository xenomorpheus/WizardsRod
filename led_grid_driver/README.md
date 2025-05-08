
Simple Script to run a LED display on a Raspberry Pi

Run Script:

   PYTHONPATH=./APA102_Pi:. ./led_grid_demo.py

Produces the following patterns:

  HAL9000
  Knight Rider

  (Planned)
  Galileo Thermometer
    Show the temperature. Have digital display at the bottom.
  Sand falling in hour glass
  Two liquids of different colours and densities. One run up. Other run down.



Play a sprite:

   PYTHONPATH=./APA102Pi:. ./sprite_player_demo --sprite sprite/fire_3x100_18.png


Software Requirements:

    APA102_Pi package. Put it somewhere on the PYTHONPATH
    https://github.com/tinue/APA102_Pi

Hardware Requirements:

    Raspberry Pi (of course)
    APA102 LED Strip
       Suggestion is 300 LEDs (5 meters)
       Cut strip into 3 x 100 LEDS, and form S pattern.
    3.3volt to 5 volt Logic Level shifter. Minimum 2 channels.
    5 volt supply for LEDs. The more amps, the more LEDs you can have illuminated at once.
    Power supply for Pi.

