import machine
import utime
import network
from secrets import *
import ubinascii

led = machine.Pin("LED", machine.Pin.OUT)

for _ in range(10):
    led.toggle()
    utime.sleep(0.1)
    
secrets_dict = get_secrets()
wifi_name = secrets_dict["network_name"]
wifi_password = secrets_dict["network_password"]


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_name, wifi_password)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Trying to connect", end="")
    utime.sleep(0.25)
    for _ in range(3):
        print(".", end="")
        utime.sleep(0.25)
    print()
    utime.sleep(0.25)
        

print(wlan.ifconfig())

mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(mac)