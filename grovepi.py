import grovepi
import pyaudio
import numpy as np
import time

MORSE_CODE_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}

SHORT_TAP_THRESHOLD = 0.1  # seconds
LONG_TAP_THRESHOLD = 3 * SHORT_TAP_THRESHOLD

def record_audio(duration):
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)
    frames = []
    for i in range(int(RATE / CHUNK_SIZE * duration)):
        data = stream.read(CHUNK_SIZE)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return np.frombuffer(b''.join(frames), dtype=np.int16)

def detect_taps(signal):
    is_tap = False
    tap_start_time = None
    taps = []
    for i in range(1, len(signal)):
        if signal[i] > 0 and signal[i - 1] <= 0:
            # Start of a new sound wave
            if tap_start_time is None:
                tap_start_time = time.time()
        elif signal[i] <= 0 and signal[i - 1] > 0:
            # End of a sound wave
            tap_duration = time.time() - tap_start_time
            if tap_duration > SHORT_TAP_THRESHOLD and tap_duration < LONG_TAP_THRESHOLD:
                taps.append('.')
            elif tap_duration >= LONG_TAP_THRESHOLD:
                taps.append('-')
            tap_start_time = None
    return taps

def decode_morse(taps):
    morse_code = ''.join(taps)
    message = ''
    for code in morse_code.split(' '):
        if code in MORSE_CODE_DICT:
            message += MORSE_CODE_DICT[code]
        else:
            message += '?'
    return message

if __name__ == '__main__':
    sound_sensor = 1  # Connect the GrovePi sound sensor to port A0
    grovepi.pinMode(sound_sensor, "INPUT")

    while True:
        sensor_value = grovepi.analogRead(sound_sensor)
        print (sensor_value)
        # print('Recording...')
        # signal = record_audio(duration=1)  # Record audio for 1 second
        # taps = detect_taps(signal)
        # message = decode_morse(taps)
        # print(f'Decoded message: {message}')