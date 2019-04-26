import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import stats, interpolate
import serial
import numpy as np

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

# 1. Create model to convert pixels into wavelengths
pixels = [21, 37, 40, 50, 70, 72, 95, 110, 146]
wavelengths_calibration = [365, 405, 410, 434, 486, 500, 546, 579, 656]
slope, intercept, r_value, p_value, std_err = stats.linregress(pixels, wavelengths_calibration)

# 2. Create model to calculate real intensity
wavelengths_intensity = 305 + np.array([14,38,47,59,70,84,95,100,106,115,121,131,140,148,161,174,182,189,195,210,230,238,247,255,266,275,282,300,317,348,374,400,431,469,518,562])
intensities = 565 - np.array([355,263,225,170,112,56,26,20,16,20,26,34,41,35,17,4,0,3,10,55,110,124,132,128,121,118,122,143,169,225,282,338,393,450,504,525])
intensities_scaled = intensities / intensities.max(axis=0) * 100
f = interpolate.interp1d(wavelengths_intensity, intensities_scaled, kind='cubic')

# 3. Setup serial port and figure plot
try:
    ser = serial.Serial('COM3', baudrate=115200, timeout=1)
except Exception as e:
    print(e)
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 4. Calculate wavelengths and real intensities
x_in = np.linspace(1, 201, 200)
wavelengths = slope * x_in + intercept
percent = f(wavelengths)
y_in = np.zeros((1, 201))

# 5. Animation function
print('Started')
def animate(i, x, y):
    try:
        ax.clear()
        # Draw spectral lines
        for i in range(len(wavelengths_calibration)):
            rgb = wavelength_to_rgb(wavelengths_calibration[i], gamma=0.8)
            ax.axvline(x=wavelengths_calibration[i], linewidth=2, color=np.array(rgb)/max(rgb))

        ax.set_ylim(0, 1050)
        data = ser.readline()
        data = data.split(b',')
        data = data[1:201]
        y_in = [int(p) for p in data]
        intensities = y_in / percent * 100
        ax.plot(wavelengths, intensities)
    except Exception as e:
        print(e)

# 5. Animate data
ani = animation.FuncAnimation(fig, animate, fargs=(x_in, y_in), interval=200)
plt.show()
