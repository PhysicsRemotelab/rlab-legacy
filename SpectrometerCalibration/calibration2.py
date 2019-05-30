import numpy as np
import matplotlib.pyplot as plt

wavelength = np.round(np.genfromtxt('SpectrometerCalibration/xval.txt', delimiter='\n'))
wavelength = wavelength * 10**-9
#wavelength = np.arange(1e-9, 3e-6, 1e-9) 
intensity_uncalibrated = np.genfromtxt('SpectrometerCalibration/yval.txt', delimiter=',')

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
T = 1800
intensity_blackbody = 2.0*h*c**2 / ( (wavelength**5) * (np.exp(h*c/(wavelength*k*T)) - 1.0) ) * 10e-9

coef = np.divide(intensity_blackbody, intensity_uncalibrated)
print(coef)
intensity = coef * intensity_uncalibrated

plt.title('Must keha temperatuuril T = 1800 K')
plt.xlabel("Lainepikkus (um)")
plt.ylabel("Kiirgus (kW * sr-1 * m-2 * nm-1)")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.plot(wavelength, intensity_uncalibrated)
plt.plot(wavelength, intensity_blackbody)
plt.plot(wavelength, coef)
plt.grid()
plt.show()
