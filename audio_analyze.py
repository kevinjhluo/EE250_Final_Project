import numpy as np
import scipy.io.wavfile as wavfile

# Load audio file
sampling_freq, audio = wavfile.read('audio.wav')

# Define parameters
window_size = int(sampling_freq * 0.1)  # Sampling window of 200ms
dash_threshold = 20000
dot_threshold = 5000
#silence_threshold = int(sampling_freq * 10)  # Silence threshold of 1 second
morse_code = ''
#is_silence = False

# Iterate over the audio samples with the defined window size
for i in range(0, len(audio), window_size):
    window = audio[i:i+window_size]
    max_amp = np.max(np.abs(window))
    print(max_amp)
    if max_amp > dash_threshold:
        morse_code += '-'
       # is_silence = False
    elif max_amp > dot_threshold:
        morse_code += '.'
        #is_silence = False
    # else:
    #     if not is_silence:
    #         is_silence = True
    #         if len(morse_code) > 0 and morse_code[-1] != ' ':
    #             morse_code += ' '
        
    # # Check for silence between two spikes
    # if is_silence and i < len(audio) - silence_threshold:
    #     silence_window = audio[i+window_size:i+window_size+silence_threshold]
    #     if np.max(np.abs(silence_window)) > dot_threshold:
    #         is_silence = False
    
# Remove duplicate dots and dashes
morse_code = ''.join([morse_code[i] for i in range(len(morse_code)) if i == 0 or morse_code[i] != morse_code[i-1]])

print(morse_code)
