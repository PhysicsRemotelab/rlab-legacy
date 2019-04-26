import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

pixels = [21, 37, 40, 50, 70, 72, 95, 110, 146]
wavelengths = [365, 405, 410, 434, 486, 500, 546, 579, 656]
slope, intercept, r_value, p_value, std_err = stats.linregress(pixels, wavelengths)

real_pixels = np.linspace(0, 150, 151)
real_wavelengths = slope * real_pixels + intercept

plt.scatter(pixels, wavelengths)
plt.plot(real_pixels, real_wavelengths, 'r')
plt.show()
