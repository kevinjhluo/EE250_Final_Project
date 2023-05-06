import matplotlib.pyplot as plt
import librosa

# Load audio file
audio_file = "audio.wav"
audio, sr = librosa.load(audio_file)

# Create a time axis in seconds
time = librosa.times_like(audio, sr=sr)

# Plot waveform
plt.plot(time, audio)

# Add labels and title
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform of Audio File")

# Display plot
plt.show()
