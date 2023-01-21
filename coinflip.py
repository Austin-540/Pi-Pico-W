from machine import Pin, PWM
import utime
import random
score = 0
onboard_led = machine.Pin("LED", machine.Pin.OUT)

red_led = machine.Pin(17, machine.Pin.OUT)
green_led = machine.Pin(16, machine.Pin.OUT)
white_led = machine.Pin(22, machine.Pin.OUT)
buzzer = PWM(Pin(15))
buzzer.freq(800)
buzzer.duty_u16(1000)
utime.sleep(0.2)
buzzer.duty_u16(0)

red_led.on()
utime.sleep(0.2)
green_led.on()
utime.sleep(0.2)


LEDs = [red_led, green_led, white_led]

def all_off():
    for i in range(len(LEDs)):
        LEDs[i].off()
    
all_off()
utime.sleep(2)


button1 = Pin(0, Pin.IN, Pin.PULL_UP)
button2 = Pin(1, Pin.IN, Pin.PULL_UP)

def button1_press(var):
    global pick
    pick = "1"

def button2_press(var):
    global pick
    pick = "2"

button1.irq(trigger=button1.IRQ_FALLING, handler=button1_press)
button2.irq(trigger=button2.IRQ_FALLING, handler=button2_press)


while True:
    pick = ""
    white_led.on()
    buzzer.duty_u16(1000)
    utime.sleep(0.6)
    white_led.off()
    buzzer.duty_u16(0)
    utime.sleep(0.6)
    white_led.on()
    buzzer.duty_u16(1000)
    utime.sleep(0.4)
    white_led.off()
    buzzer.duty_u16(0)
    utime.sleep(0.4)
    white_led.on()
    buzzer.freq(300)
    buzzer.duty_u16(1000)
    utime.sleep(0.2)
    white_led.off()
    buzzer.duty_u16(0)
    buzzer.freq (800)
    utime.sleep(0.5)
    
    utime.sleep(0.7)
    if pick == "":
        print("No guess")
    
    elif pick == "1" or pick == "2":
        if random.randint(1,2) == 1:
            print("Win Score:", score+1)
            score += 1
            green_led.on()
            utime.sleep(0.5)
            green_led.off()
        else:
            print("Lose")
            red_led.on()
            utime.sleep(0.5)
            red_led.off()
    
    for _ in range(score):
        onboard_led.on()
        utime.sleep(0.2)
        onboard_led.off()
        utime.sleep(0.2)
    utime.sleep(3)
    
    
    
    
    


