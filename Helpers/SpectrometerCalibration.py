import os, glob, serial
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

ser = serial.Serial('COM3', baudrate=115200, timeout=1)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(1, 286, 286)
y = []

print('Started')
def animate(i, x, y):
    try:
        ax.clear()
        ax.set_ylim(0, 1050)
        data = ser.readline()
        data = data.split(b',')
        data = data[1:287]
        y = [int(p) for p in data]
        ax.plot(x, y)
    except Exception as e:
        print(e)

ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=100)
plt.show()
