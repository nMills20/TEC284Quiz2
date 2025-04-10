#impport gpiozero library
import time
from gpiozero import RGBLED, Button

#set up LED with GPIO
led = RGBLED (red = 5, green = 6, blue = 26)

#set up buttons
red_button = Button(22)
green_button = Button(27)
blue_button = Button(17)

#function for LED color
def update_led():
    r = 1 if red_button.is_pressed else 0
    g = 1 if green_button.is_pressed else 0
    b = 1 if blue_button.is_pressed else 0
    led.color = (r,g,b)
    
#create loop for update_led function
while True:
    update_led()
    time.sleep(0.1)