import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats

img = mpimg.imread('HeatcamImageParsing/heatcam.jpg')
n = np.shape(img)

xc = 160
yc = 120

rvals = np.arange(30, 80, 1)
phivals = np.arange(0, 2*np.pi, 1*np.pi/180)
radius = np.log(rvals)
temperature = np.zeros(len(rvals))

for i in range(len(rvals)):
    xr = (rvals[i] * np.sin(phivals) + xc).astype(int)
    yr = (rvals[i] * np.cos(phivals) + yc).astype(int)
    avg = np.mean(img[xr, yr])
    temperature[i] = avg

slope, intercept, r_value, p_value, std_err = stats.linregress(radius[0:10,], temperature[0:10,])
print(slope)
print(intercept)
line_y = slope * radius + intercept

plt.plot(radius, temperature)
plt.plot(radius[0:10,], line_y[0:10,], 'r')
plt.title('Temperatuuri ja raadiuse suhe')
plt.xlabel('Raadius (pikslid)')
plt.ylabel('Temperatuur (pikslid)')
plt.grid()
plt.show()
