import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd

# Parameters
fs = 44100
duration = 5
f1, f2 = 800, 1000

# Generate time axis
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate signal
signal = 0.5 * (np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t))

# Save to file
write("2tone.wav", fs, (signal * 32767).astype(np.int16))

sd.play(signal, fs)
sd.wait()
