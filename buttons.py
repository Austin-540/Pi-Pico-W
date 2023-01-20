from picozero import Button
from time import sleep
print("Hello world")

button = Button(12)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
    sleep(0.1)
