import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import interpolate
import serial
import time
from wavelengthtorgb import wavelength_to_rgb

# 1. Convert pixels into wavelengths
x = (2.35 * np.linspace(10, 250, 240) + 319.16) * 10e-10

# 2. Create model to describe uncalibrated line
wavelength = np.round(np.genfromtxt('SpectrometerCalibration/xval.txt', delimiter='\n'))
wavelength = wavelength * 10e-10
intensity = np.genfromtxt('SpectrometerCalibration/yval.txt', delimiter=',')
uncalibrated_line = interpolate.interp1d(wavelength, intensity, kind='cubic')

# 3. Create model to describe black body line 
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
T = 1700 + 273
blackbody_line = 2.0*h*c**2 / ((x**5) * (np.exp(h*c/(x*k*T)) - 1.0)) * 10e-9

# 4. Calculate coefficients and function
uncalibrated_y = uncalibrated_line(x)
coef = blackbody_line / uncalibrated_y
coef_func = interpolate.interp1d(x, coef, kind='cubic')

# 5. Setup serial port
try:
    ser = serial.Serial('COM3', baudrate=115200, timeout=1)
except Exception as e:
    print(e)
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 6. Calculate wavelengths and real intensities
wavelengths = (2.35 * np.linspace(10, 250, 240) + 319.16) * 10e-10
percent = coef_func(wavelengths)
y_in = np.zeros((0, 240))

# 7. Animation function
print('Started')
wavelengths_calibration = np.array([365, 405, 410, 434, 486, 500, 546, 579, 656])
i = 0
start = time.time()

def animate(i, x, y):
    try:
        data = ser.readline()
        ser.flushInput()

        data2 = data.split(b',')
        data3 = data2[10:250]
        
        if len(data3) ==  240:
            ax.clear()
            ax.grid()
            #ax.set_ylim(0, 1000)
            #ax.set_xlim(300, 800)
            plt.ticklabel_format(style='sci', axis='x', scilimits=(-9,-9))
            y_in = [int(p) for p in data3]
            real_intensities = percent * y_in
            #real_intensities = real_intensities / max(real_intensities) * 100
            #ax.plot(wavelengths, percent)
            ax.plot(wavelengths, y_in)
            ax.plot(wavelengths, real_intensities)

            # Draw spectral lines
            for j in range(len(wavelengths_calibration)):
                rgb = wavelength_to_rgb(wavelengths_calibration[j], gamma=0.8)
                ax.axvline(x=wavelengths_calibration[j] * 10e-10, linewidth=2, color=np.array(rgb)/max(rgb))

            i+=1
            #print(i, time.time() - start)

    except Exception as e:
        print(e)

# 8. Animate data
ani = animation.FuncAnimation(fig, animate, fargs=(wavelengths, y_in), interval=20)

plt.show()
