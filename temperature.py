from machine import ADC
import utime

tempsensor = ADC(4)
conversion_factor = 3.3 / 65535

while True:
    currentvoltage = tempsensor.read_u16() * conversion_factor
    temp = 27 - ((currentvoltage - 0.706)/0.001721)
    print(str("{:.1f} °C".format(temp)))
    utime.sleep(2)