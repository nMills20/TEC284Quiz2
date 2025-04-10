#impport gpiozero library
import time
from gpiozero import RGBLED, Button

#set up LED with GPIO
led = RGBLED (red = 5, green = 6, blue = 26)

#set up buttons
red_button = Button(17)
green_button = Button(27)
blue_button = Button(22)