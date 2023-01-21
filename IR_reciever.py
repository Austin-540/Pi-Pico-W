import time
from machine import Pin
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses

red = machine.Pin(16, machine.Pin.OUT)

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
    if data < 0:  # NEC protocol sends repeat codes.
        print('Repeat code.')
    else:
        print('Data {:02x} Addr {:04x}'.format(data, addr))
        ir_code_label = codes[str(data)]
        print(ir_code_label)
        
        if ir_code_label == "on":
            red.on()
        elif ir_code_label == "off":
            red.off()
        
        

ir = NEC_8(Pin(15, Pin.IN), callback)

