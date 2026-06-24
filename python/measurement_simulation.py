import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

rows = 25
cols = 2 * rows + 1

psi = np.zeros((rows, cols), dtype=complex)
psi[0, cols // 2] = 1.0

BS = (1 / np.sqrt(2)) * np.array([[1, 1j],
                                  [1j, 1]])

history = []

for r in range(rows - 1):
    new_psi = np.zeros_like(psi)
    for c in range(1, cols - 1):
        if psi[r, c] != 0:
            out = BS @ np.array([psi[r, c], 0])
            new_psi[r + 1, c - 1] += out[0]
            new_psi[r + 1, c + 1] += out[1]
    psi = new_psi
    history.append(np.abs(psi)**2)

prob = np.abs(psi[-1])**2
prob /= prob.sum()
final_pos = np.random.choice(cols, p=prob)

path = [(rows - 1, final_pos)]
c = final_pos

for r in range(rows - 1, 0, -1):
    left = abs(psi[r - 1, c + 1])**2 if c + 1 < cols else 0
    right = abs(psi[r - 1, c - 1])**2 if c - 1 >= 0 else 0
    if left + right == 0:
        break
    p_left = left / (left + right)
    if np.random.rand() < p_left:
        c += 1
    else:
        c -= 1
    path.append((r - 1, c))

path = path[::-1]

fig, ax = plt.subplots()
img = ax.imshow(history[0], cmap="gray", origin="upper")
line, = ax.plot([], [], color="lime", lw=2)

ax.set_title("Quantum Galton Board: Wave + Photon Path")

def update(frame):
    img.set_data(history[frame])

    if frame < len(path):
        ys, xs = zip(*path[:frame+1])
        line.set_data(xs, ys)

    return img, line

ani = FuncAnimation(fig, update, frames=len(history), interval=120)
plt.show()
