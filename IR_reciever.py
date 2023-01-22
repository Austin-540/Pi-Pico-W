import time
from machine import Pin
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses


led_r = machine.Pin(22, machine.Pin.OUT)
led_g = machine.Pin(26, machine.Pin.OUT)
led_b = machine.Pin(27, machine.Pin.OUT)

codes = {
    "13": "on",
    "31": "off",
    "9": "br_up",
    "29": "br_down",
    "25": "red",
    "27": "green",
    "17": "blue",
    "21": "white",
    "77": "flash",
    "0": "strobe",
    "26": "fade",
    "12": "smooth"
    }

def callback(data, addr, ctrl):
    global state
    if data < 0:  # NEC protocol sends repeat codes.
        print('Repeat code.')
    else:
        print('Data {:02x} Addr {:04x}'.format(data, addr))
        ir_code_label = codes[str(data)]
        print(ir_code_label)
        
        
        if ir_code_label == "on":
            if state == "white":
                led_r.on()
                led_g.on()
                led_b.on()
            elif state == "red":
                led_r.on()
            elif state == "green":
                led_g.on()
            else:
                led_b.on()
                
        elif ir_code_label == "off":
            led_r.off()
            led_g.off()
            led_b.off()
        elif ir_code_label == "red":
            state = "red"
            led_r.on()
            led_g.off()
            led_b.off()
        elif ir_code_label == "green":
            state = "green"
            led_g.on()
            led_r.off()
            led_b.off()
        elif ir_code_label == "blue":
            state = "blue"
            led_b.on()
            led_r.off()
            led_g.off()
        elif ir_code_label == "white":
            state = "white"
            led_r.on()
            led_g.on()
            led_b.on()
            
global state
state = "white"
ir = NEC_8(Pin(15, Pin.IN), callback)

