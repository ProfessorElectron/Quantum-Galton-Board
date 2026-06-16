import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
rows = 40
cols = 2 * rows + 1

# Initialize wavefunction
psi = np.zeros((rows, cols), dtype=complex)
psi[0, cols // 2] = 1.0 + 0j

# Beam splitter (introduces phase → interference)
BS = (1 / np.sqrt(2)) * np.array([[1, 1j],
                                  [1j, 1]])

# Store history
history = [np.abs(psi)**2]

for r in range(rows - 1):
    new_psi = np.zeros_like(psi)

    for c in range(1, cols - 1):
        amp = psi[r, c]
        if amp != 0:
            out = BS @ np.array([amp, 0])
            new_psi[r + 1, c - 1] += out[0]
            new_psi[r + 1, c + 1] += out[1]

    psi = new_psi
    history.append(np.abs(psi)**2)

# --- Animation ---
fig, ax = plt.subplots()
img = ax.imshow(history[0], cmap="inferno", origin="upper")
ax.set_title("Quantum Galton Board — Photon Interference")
ax.set_xlabel("Position")
ax.set_ylabel("Depth")

def update(frame):
    img.set_data(history[frame])
    return img,

ani = FuncAnimation(fig, update, frames=len(history), interval=120)
plt.show()
out *= np.exp(1j * np.random.normal(0, 0.05))
