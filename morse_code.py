import machine
led = machine.Pin("LED", machine.Pin.OUT)
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
          "----.": "9"}


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
