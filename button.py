import time
import grovepi
import paho.mqtt.client as mqtt

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
    morse_letters = morse_code.strip().split()
    for code in morse_letters:
        for letter, morse in MORSE_CODE_DICT.items():
            if code == morse:
                decoded_message += letter
    return decoded_message

   
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

# Call the main function
if __name__ == '__main__':
    message = ''
    print ('Press the message you wish to encode')
    start_time = time.time()
    while time.time() - start_time < 10:
        message += str(grovepi.digitalRead(button))
        time.sleep(0.2)
    morse_code = decode_morse_code(message)
    print('The decoded message is:', morse_code)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.publish("button/morse_code", f"{morse_code}")

