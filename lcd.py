import utime
import machine

from machine import I2C, ADC, Timer
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

tempsensor = ADC(4)
conversion_factor = 3.3 / 65535

def hello_world(temperature):
    lcd.clear()
    lcd.move_to(2,0)
    lcd.putstr("Hello World!")
    lcd.move_to(0,1)
    lcd.putstr("Its      degrees")


def update_temp():
    print("Temp Tick")
    currentvoltage = tempsensor.read_u16() * conversion_factor
    temp = 27 - ((currentvoltage - 0.706)/0.001721)
    lcd.move_to(4,1)
    lcd.putstr("{:.1f}".format(temp))
    print("Temp: ", temp)

def temp_tick(var):
    print("Temp Tick")
    currentvoltage = tempsensor.read_u16() * conversion_factor
    temp = 27 - ((currentvoltage - 0.706)/0.001721)
    update_temp(temp)
    
Timer().init(freq=1, mode=Timer.PERIODIC, callback=temp_tick)

#my custom display commands
#clear screen

hello_world("")

currentvoltage = tempsensor.read_u16() * conversion_factor
temp = 27 - ((currentvoltage - 0.706)/0.001721)
update_temp()

    
while True:
    utime.sleep(4)
    print("Time.sleep finished")
    update_temp()