import machine
import utime
import network
from secrets import *
import socket

from machine import ADC, Timer
import utime

tempsensor = ADC(4)
conversion_factor = 3.3 / 65535

def temp_tick(var):
    global html
    currentvoltage = tempsensor.read_u16() * conversion_factor
    temp = 27 - ((currentvoltage - 0.706)/0.001721)
    html = """<!DOCTYPE html>
<html>
    <head><meta http-equiv="refresh" content="5">
    <title> Pico W </title> </head>
    <body> <h1> The Pico W </h1>
    <p><h2><a href="/light/on"> Turn the LED on! </a></p>
    <p><a href="/light/off"> Turn the LED off! </a></h2></p>
    <p></p>
    <p> The current temperature of the Pi Pico W is {:.1f} degrees celsius.
    </body>
</html>""".format(temp)

Timer().init(freq=0.5, mode=Timer.PERIODIC, callback=temp_tick)

led = machine.Pin("LED", machine.Pin.OUT)

temp_tick(5)

secrets_dict = get_secrets()
wifi_name = secrets_dict["network_name"]
wifi_password = secrets_dict["network_password"]


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_name, wifi_password)

max_wait = 10 #seconds

while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("Trying to connect...")
    utime.sleep(1)
    
if wlan.status() !=3:
    print("Connection Failed!")

else:
    print("Connected")
    print("IP = " + wlan.ifconfig()[0])
    


sta_if = network.WLAN(network.STA_IF)
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    try:
        cl, addr = s.accept()
        print("Client connected from ", addr)
        request = cl.recv(1024)
        print(request)
        
        request = str(request)
        led_on = request.find("/light/on")
        led_off = request.find("/light/off")
        print("led on = " + str(led_on))
        print("led off = " + str(led_off))
        
        if led_on == 6:
            print("LED on")
            led.on()
            stateis = "LED ON"
        
        if led_off == 6:
            print("LED off")
            led.off()
            stateis = "LED OFF"
            
        try:
            response = html % stateis
        except:
            response = html
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print("Connection closed")


