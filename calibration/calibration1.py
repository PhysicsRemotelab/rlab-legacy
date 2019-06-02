import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import interpolate
import serial

#pixels = np.linspace(0, 240, 240)
#pixels = np.round((x_dark - 316.19) / 2.34)

# 1. Load lamp data
x_dark = np.genfromtxt('x_dark2.csv', delimiter='\n')
y_dark = np.genfromtxt('y_dark2.csv', delimiter='\n')
x_lamp = np.genfromtxt('x_lamp2.csv', delimiter='\n')
y_lamp = np.genfromtxt('y_lamp2.csv', delimiter='\n')

# 2. Calculate black body intensity and normalize
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
T = 1700
wavelength = x_lamp * 10**-9
intensity_blackbody = 2.0*h*c**2 / ( (wavelength**5) * (np.exp(h*c/(wavelength*k*T)) - 1.0))
intensity_blackbody = intensity_blackbody / np.max(intensity_blackbody)

# 3. Normalize lamp intensity
intensity_lamp = y_lamp - y_dark - min(y_lamp - y_dark)
intensity_lamp = intensity_lamp / np.max(intensity_lamp)

# 4. Calculate coefficients
coef = intensity_blackbody / intensity_lamp
coef_func = interpolate.interp1d(x_lamp, coef, kind='cubic') 

# 5. Plot
line1 = plt.plot(x_lamp, intensity_lamp)
line2 = plt.plot(x_lamp, intensity_blackbody)
#line3 = plt.plot(x_lamp, coef)
plt.legend(['Lambi intensiivsus', 'Must keha T=1800K', 'Koefitsent'])
plt.xlabel("Lainepikkus (nm)")
plt.ylabel("Intensiivsus (0-1)")
plt.grid()
plt.show()
