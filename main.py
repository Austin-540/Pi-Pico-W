import machine
import utime
import network
from secrets import *
import socket

led = machine.Pin("LED", machine.Pin.OUT)

for _ in range(5):
    led.toggle()
    utime.sleep(0.1)
    
secrets_dict = get_secrets()
wifi_name = secrets_dict["network_name"]
wifi_password = secrets_dict["network_password"]


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_name, wifi_password)

max_wait = 10 #seconds

led.on()
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("Trying to connect...")
    utime.sleep(1)
    
if wlan.status() !=3:
    print("Connection Failed!")
    while True:
        led.toggle()
        utime.sleep(0.2)
else:
    print("Connected")
    print("IP = " + wlan.ifconfig()[0])
    led.off()


html = """<!DOCTYPE html>
<html>
    <head> <title> Pico W </title> </head>
    <body> <h1> The Pico W </h1>
    <p> Hello world! </p>
    </body>
</html>"""

sta_if = network.WLAN(network.STA_IF)
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    cl, addr = s.accept()
    cl_file = cl.makefile("rwb", 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    response = html
    cl.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
    cl.send(response)
    cl.close()



