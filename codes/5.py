import numpy as np
import matplotlib.pyplot as plt

# Given parameters
s1 = -0.3421 - 0.4276j
s2 = -0.6841 + 0.0000j
s3 = -0.3421 + 1.0322j

epsilon = 0.3
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

G_LP = 0.4166
num = G_LP

Omega_p1 = 0.5913
Omega_p2 = 0.702

Omega_s1 = 0.5662
Omega_s2 = 0.7361

# Define parameters for transformation
B = 0.1107
Omega0 = 0.644

# Perform transformation to get s_L
s_L = (1j * w)**2 + Omega0**2
s_L = s_L / (B * (1j * w))

# Band pass gain
G_bp = 1.0370

# Substitute s = jw into H(s)
H = G_bp * (num / np.polyval(den, s_L))

# Plot magnitude response for H(s)
plt.figure()
plt.plot(w, abs(H), linewidth=1)
plt.title('Band Pass Filter')
plt.xlabel('Analog Frequency ($\Omega$)')
plt.ylabel('|H_{a,BP}($\Omega$)|')
plt.grid(True)
plt.ylim(0, 1.2)
plt.savefig("../figs/5.png")
