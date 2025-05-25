# 🔊 Two-Tone Signal Analysis at Varying Playback Volumes

## 📌 Introduction

This project presents an analysis of a two-tone signal that was recorded at five different playback volumes: **10%, 30%, 50%, 70%, and 90%**. The study focuses on signal behavior under changing amplitude conditions, with a particular interest in **intercept point detection** and **dominant frequency analysis**.

---

## 🎛️ Signal Generation, Playback, and Recording

A synthetic two-tone signal was generated in Python, composed of **800 Hz** and **1000 Hz** frequencies. Key parameters:

- **Sample rate**: 44.1 kHz  
- **Duration**: 5 seconds  
- **Playback device**: Laptop  
- **Recording device**: Mobile phone  

Recordings were made at the following laptop volume settings:

- `10%`, `30%`, `50%`, `70%`, `90%`

These five audio files form the dataset for signal analysis and intercept point extraction.

---

## ⚡ Intercept Point Extraction

Each audio recording was analyzed to detect **zero-crossings**, which are the points where the signal waveform crosses the zero-amplitude axis.

The first three odd intercept points for each recording are:

- `recorded_volume_10.wav`: [2236, 2264, 2276]  
- `recorded_volume_30.wav`: [2274, 2285, 2298]  
- `recorded_volume_50.wav`: [2225, 2232, 2270]  
- `recorded_volume_70.wav`: [2306, 2318, 2355]  
- `recorded_volume_90.wav`: [2215, 2271, 2277]

This comparison provides insight into how volume levels affect waveform timing and zero-crossing consistency.

---

## 📈 Frequency Analysis

Using **Fast Fourier Transform (FFT)**, each recording was analyzed to extract its **dominant frequency components**:

- Audio waveforms were normalized.
- FFT was applied to compute the frequency spectrum.
- Frequency magnitudes were visualized up to 2000 Hz.
- The **most prominent frequency** and its magnitude were identified for each recording.

This analysis enables comparison of frequency integrity and signal consistency across different playback volumes.

---

## Paper 

Full paper available here: [DSP Analysis](dspproject.pdf)

