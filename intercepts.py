import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

def extract_intercepts(filename):
    fs, data = read(filename)
    data = data.astype(np.float32)

    if data.ndim > 1:
        data = data[:, 0]

    data = data / np.max(np.abs(data))

    intercepts = np.where(np.diff(np.sign(data)))[0]
    odd_intercepts = intercepts[2::2]

    plt.figure(figsize=(10, 4))
    plt.plot(data[:4000], label="Signal")
    plt.plot(odd_intercepts[:3], data[odd_intercepts[:3]], 'ro', label="Odd Intercepts")
    plt.title(f"Odd Intercepts in {filename}")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude (Normalized)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    return odd_intercepts

# Loop through all volume levels
for vol in [10, 30, 50, 70, 90]:
    filename = f"recorded_volume_{vol}.wav"
    print(f"Intercepts for volume {vol}%:")
    intercepts = extract_intercepts(filename)
    print("First 3 odd intercept indices:", intercepts[:3])
