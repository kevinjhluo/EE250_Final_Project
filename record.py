import sounddevice as sd
import soundfile as sf

filename = "audio.wav"
duration = 10  # Recording duration in seconds
samplerate = 44100  # Sample rate of the recording

def record_audio():
    print("Recording started.")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()  # Wait for the recording to complete
    sf.write(filename, recording, samplerate)  # Save the recording to a WAV file
    print(f"Recording saved to {filename}")

if __name__ == "__main__":
    record_audio()