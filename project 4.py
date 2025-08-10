import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# data
x = np.linspace(0, 10, 200)
y = np.sin(x)

# create figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.set_title("Animated Sine Wave")

# function to update the frame
def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

# make the animation
ani = FuncAnimation(fig, update, frames=len(x), interval=30, blit=True)

plt.show()
