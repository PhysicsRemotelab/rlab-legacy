import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

pixels = [42, 50, 71, 148, 39, 51, 96, 110]
wavelengths = [410, 434, 486, 656, 405, 435, 546, 578]
slope, intercept, r_value, p_value, std_err = stats.linregress(pixels, wavelengths)
print(slope)
print(intercept)
real_pixels = np.linspace(0, 150, 151)
real_wavelengths = slope * real_pixels + intercept

plt.title('Lainepikkuste ja spkektromeetri anduri näidu sõltuvus')
plt.xlabel("Spektromeetri näit")
plt.ylabel("Lainepikkus (nm)")
plt.scatter(pixels, wavelengths)
plt.plot(real_pixels, real_wavelengths, 'r')
plt.grid()
plt.show()


