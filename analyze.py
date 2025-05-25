import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

def analyze_fft(filename):
    fs, data = read(filename)
    data = data.astype(np.float32)

    if data.ndim > 1:
        data = data[:, 0]

    data = data / np.max(np.abs(data))

    N = len(data)
    fft_result = np.fft.fft(data)
    fft_magnitude = np.abs(fft_result)[:N // 2]
    freqs = np.fft.fftfreq(N, 1 / fs)[:N // 2]

    plt.figure(figsize=(10, 4))
    plt.plot(freqs, fft_magnitude)
    plt.title(f"FFT of {filename}")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.xlim(0, 2000)  # Adjust for your range of interest
    plt.tight_layout()
    plt.show()

    top_indices = np.argsort(fft_magnitude)[-5:][::-1]
    top_index = np.argmax(fft_magnitude)
    print(f"Top Frequency in {filename}:")
    print(f"  Frequency: {freqs[top_index]:.1f} Hz, Magnitude: {fft_magnitude[top_index]:.2f}")
    print()

# Loop through all volume levels
for vol in [10, 30, 50, 70, 90]:
    analyze_fft(f"recorded_volume_{vol}.wav")
