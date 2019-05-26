import numpy as np
import matplotlib.pyplot as plt

wavelength = np.round(np.genfromtxt('Helpers/xval.txt', delimiter='\n'))
wavelength = wavelength * 10**-9
#wavelength = np.arange(1e-9, 3e-6, 1e-9) 
intensity = np.genfromtxt('Helpers/yval.txt', delimiter=',')

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
T = 1700 + 273
intensity_blackbody = 2.0*h*c**2 / ( (wavelength**5) * (np.exp(h*c/(wavelength*k*T)) - 1.0) )

coef = intensity_blackbody / intensity 
intensity = coef * intensity

plt.title('Must keha temperatuuril T = 1972 K')
plt.xlabel("Lainepikkus (um)")
plt.ylabel("Kiirgus (kW * sr-1 * m-2 * nm-1)")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.plot(wavelength, intensity)
plt.grid()
plt.show()
