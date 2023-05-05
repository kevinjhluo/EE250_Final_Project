import time
import grovepi

# Define the Morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

# Define the GrovePi button input
button = 4

# Set the pin mode for the button
grovepi.pinMode(button,"INPUT")


# Define the function to decode a message from Morse code
def decode_morse_code(morse_code):
    message = ''
    morse_code_words = morse_code.split(' ')
    for word in morse_code_words:
        if word == '':
            message += ' '
        else:
            for letter, code in MORSE_CODE_DICT.items():
                if code == word:
                    message += letter
    return message

# Define the main function
def main():
    # Wait for the button to be pressed
    print('Press the button to start encoding a message in Morse code.')
    while grovepi.digitalRead(button) == 0:
        time.sleep(0.1)
    
    # Start encoding the message in Morse code
    print ('Press the message you wish to encode')
    message = ''
    start_time = time.time()
    last_press_time = time.time()
    while time.time() - start_time < 5:
        button_state = grovepi.digitalRead(button)
        if button_state == 1:
            current_time = time.time()
            if current_time - last_press_time > 1:
                break
            else:
                message += '.'
        else:
            current_time = time.time()
            if current_time - last_press_time > 1:
                break
            else:
                message += '-'
        last_press_time = current_time
    
    
    # Decode the Morse code message and print it
    decoded_message = decode_morse_code(morse_code)
    print('The decoded message is:', decoded_message)

# Call the main function
if __name__ == '__main__':
    main()
