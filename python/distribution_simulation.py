import numpy as np
import matplotlib.pyplot as plt

rows = 30
cols = 2 * rows + 1

psi = np.zeros((rows, cols), dtype=complex)

psi[0, cols // 2] = 1.0 + 0j

BS = (1 / np.sqrt(2)) * np.array([[1, 1j],
                                  [1j, 1]])

for r in range(rows - 1):
    new_psi = np.zeros_like(psi)

    for c in range(1, cols - 1):
        amp = psi[r, c]
        if amp != 0:
            out = BS @ np.array([amp, 0])

            new_psi[r + 1, c - 1] += out[0]
            new_psi[r + 1, c + 1] += out[1]

    psi = new_psi

prob = np.abs(psi[-1])**2
prob /= prob.sum()

plt.bar(range(cols), prob)
plt.title("Quantum Galton Board (Photon Interference)")
plt.xlabel("Position")
plt.ylabel("Probability")
plt.show()
