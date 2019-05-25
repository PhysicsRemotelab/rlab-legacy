import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import interpolate
import serial
import time

def wavelength_to_rgb(wavelength, gamma=0.8):
    '''This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''
    wavelength = float(wavelength)
    if wavelength >= 365 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 365) / (440 - 365)
        R = ((-(wavelength - 440) / (440 - 365)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))

# 1. Convert pixels into wavelengths
x = (2.35 * np.linspace(10, 250, 240) + 319.16) * 10e-10

# 2. Create model to describe uncalibrated line
wavelength = np.round(np.genfromtxt('Helpers/xval.txt', delimiter='\n'))
wavelength = wavelength * 10e-10
intensity = np.genfromtxt('Helpers/yval.txt', delimiter=',')
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
#coef_norm = coef / max(coef) * 100
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
y_in = np.zeros((1, 201))

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
            ax.set_ylim(0, 100)
            #ax.set_xlim(300, 800)
            plt.ticklabel_format(style='sci', axis='x', scilimits=(-9,-9))
            y_in = [int(p) for p in data3]
            real_intensities = percent * y_in
            real_intensities = real_intensities / max(real_intensities) * 100
            ax.plot(wavelengths, real_intensities)

            # Draw spectral lines
            for j in range(len(wavelengths_calibration)):
                rgb = wavelength_to_rgb(wavelengths_calibration[j], gamma=0.8)
                ax.axvline(x=wavelengths_calibration[j] * 10e-10, linewidth=2, color=np.array(rgb)/max(rgb))

            i+=1
            print(i, time.time() - start)

    except Exception as e:
        print(e)

# 8. Animate data
ani = animation.FuncAnimation(fig, animate, fargs=(wavelengths, y_in), interval=20)

plt.show()
