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
def decode_morse_code(message):
    decoded_message = ''
    num_of_ones = 0
    for char in message:
        if char == '1':
            num_of_ones += 1
        else: num_of_ones = 0
        if num_of_ones >= 3:
            decoded_message += '-'
        elif num_of_ones == 1:
            decoded_message += '.'  
    print(decoded_message)
    for letter, code in MORSE_CODE_DICT.items():
        if code == decoded_message:
            message += letter
    return message

# Define the main function
def main():
    # Wait for the button to be pressed
    message = ''
    print('Press the button to start encoding a message in Morse code.')
    while grovepi.digitalRead(button) == 0:
        time.sleep(0.1)
    
    # Start encoding the message in Morse code
    print ('Press the message you wish to encode')
    start_time = time.time()
    while time.time() - start_time < 5:
        message += str(grovepi.digitalRead(button))
        time.sleep(0.2)
        # if button_state == 1:
        #     current_time = time.time()
        #     if current_time - last_press_time > 1:
        #         break
        #     else:
        #         message += '.'
        # else:
        #     current_time = time.time()
        #     if current_time - last_press_time > 1:
        #         break
        #     else:
        #         message += '-'
        # last_press_time = current_time
    
    print (message)
    decoded_message = decode_morse_code(message)
    print('The decoded message is:', decoded_message)

# Call the main function
if __name__ == '__main__':
    main()
