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
    morse_code = ''
    num_of_ones = 0
    num_of_zeros = 0
    for char in message:
        if char == '1':
            num_of_ones += 1
            num_of_zeros = 0
        else:
            num_of_zeros += 1
            if num_of_zeros >= 4:
                morse_code += " "
                num_of_zeros = 0
            if num_of_ones >= 3:
                morse_code += '-'
            elif num_of_ones >= 1 and num_of_ones <3:
                morse_code += '.' 
            num_of_ones = 0 
    print(morse_code)
    morse_words = morse_code.split(' ')
    
    # Loop through each word and translate it to a letter
    decoded_words = []
    for morse_word in morse_words:
        decoded_word = ''
        # Split the Morse code word into letters
        morse_letters = morse_word.split(' ')
        for morse_letter in morse_letters:
            # Use the dictionary to translate the Morse code letter to a letter
            decoded_letter = MORSE_CODE_DICT.get(morse_letter)
            if decoded_letter is not None:
                decoded_word += decoded_letter
        decoded_words.append(decoded_word)
    
    # Join the decoded words together to form the final message
    decoded_message = ' '.join(decoded_words)
    return decoded_message

# Define the main function
def main():
    # Wait for the button to be pressed
    message = ''
    
    # Start encoding the message in Morse code
    print ('Press the message you wish to encode')
    start_time = time.time()
    while time.time() - start_time < 10:
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
    morse_code = decode_morse_code(message)
    print('The decoded message is:', morse_code)

# Call the main function
if __name__ == '__main__':
    main()
