import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import interpolate
import serial
from coefficients import coef_func, x_lamp, y_lamp, intensity_blackbody

# 1. Setup serial port
try:
    ser = serial.Serial('COM3', baudrate=115200, timeout=1)
except Exception as e:
    print(e)
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 2. Calculate coefficients
coef = coef_func(x_lamp)
y_in = np.zeros((0, 240))

# Animation function
print('Started')
def animate(i, x, y):
    try:
        data = ser.readline()
        ser.flushInput()
        data2 = data.split(b',')
        data3 = data2[10:250]
        
        if len(data3) ==  240:
            ax.clear()
            ax.grid()
            ax.set_ylim(0, 2000)
            #ax.set_xlim(300, 800)
            #plt.ticklabel_format(style='sci', axis='x', scilimits=(-9,-9))
            y_in = [int(p) for p in data3]
            real_intensities = np.multiply(coef * y_in, 1)
            ax.plot(x_lamp, y_in)
            ax.plot(x_lamp, y_lamp)
            ax.plot(x_lamp, real_intensities)
            ax.plot(x_lamp, intensity_blackbody * 1000)
            ax.legend(['Kalibreerimata', 'Lamp', 'Kalibreeritud', 'Must keha'])

    except Exception as e:
        print(e)

# 8. Animate data
ani = animation.FuncAnimation(fig, animate, fargs=(x_lamp, y_in), interval=20)

plt.show()
