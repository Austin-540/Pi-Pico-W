import machine
import utime
from machine import PWM, Pin
led = machine.Pin(18, machine.Pin.OUT)
buzzer = PWM(Pin(15))
buzzer.freq(500)
volume = 1000

decode = {".-": "A",
          "-...": "B",
          "-.-.": "C",
          "-..": "D",
          ".": "E",
          "..-.": "F",
          "--.": "G",
          "....": "H",
          "..": "I",
          ".---": "J",
          "-.-": "K",
          ".-..": "L",
          "--": "M",
          "-.": "N",
          "---": "O",
          ".--.": "P",
          "--.-": "Q",
          ".-.": "R",
          "...": "S",
          "-": "T",
          "..-": "U",
          "...-": "V",
          ".--": "W",
          "-..-": "X",
          "-.--": "Y",
          "--..": "Z",
          "-----": "0",
          ".----": "1",
          "..---": "2",
          "...--": "3",
          "....-": "4",
          ".....": "5",
          "-....": "6",
          "--...": "7",
          "---..": "8",
          "----.": "9",
          "/": " "
          }


encode = {v: k for k, v in decode.items()}


my_word = input("What is your word? >").upper()

my_word_list = []

for i in range(len(my_word)):
    my_word_list.append(my_word[i])

dots_and_dashes = []
    
for i in range(len(my_word_list)):
    current_letter = my_word_list[i]
    for key, value in encode.items():
        if key == current_letter:
            dots_and_dashes.append(value)

print(dots_and_dashes)


def flash_led(morse_code_letter):
    led.off()
    for char in morse_code_letter:
        if char == ".":
            led.on()
            buzzer.duty_u16(volume)
            utime.sleep(0.2)
            led.off()
            buzzer.duty_u16(0)
        if char == "-":
            led.on()
            buzzer.duty_u16(volume)
            utime.sleep(0.6)
            led.off()
            buzzer.duty_u16(0)
        if char == '/':
            utime.sleep(1)
        
        
        utime.sleep(0.2)



for i in range(len(dots_and_dashes)):
    flash_led(dots_and_dashes[i])
    utime.sleep(0.8)
