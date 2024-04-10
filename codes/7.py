import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function h_LP(n)

def h_LP(n):
    if n != 0 and -100 <= n <= 100:
        return np.sin(n * np.pi / 40) / (n * np.pi)
    else:
        return 0

# Generate values for n
n_values = np.arange(-480, 491)

# Calculate h_LP for each value of n
h_Lp = np.array([h_LP(n) for n in n_values])

# Calculate the DTFT using numpy's FFT
H_freq_response = np.fft.fftshift(np.fft.fft(h_Lp))

# Angular frequency axis (normalized)
omega_normalized = np.linspace(-np.pi/2, np.pi/2, len(n_values))

# Plotting
plt.plot(omega_normalized/np.pi, np.abs(H_freq_response))
plt.xlabel('($\omega$/pi)')
plt.ylabel('|H(r$\omega$)|')
plt.title('FIR LOW PASS FILTER')
plt.grid(True)
plt.savefig("../figs/7.png")
