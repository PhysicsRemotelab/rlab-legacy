import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('HeatcamImage/heatcam.jpg')
n = np.shape(img)

xc = 160
yc = 120

rvals = np.arange(30, 80, 1)
phivals = np.arange(0, 2*np.pi, 1*np.pi/180)

rmeans = np.zeros(len(rvals))
for i in range(len(rvals)):
    xr = (rvals[i] * np.sin(phivals) + xc).astype(int)
    yr = (rvals[i] * np.cos(phivals) + yc).astype(int)
    avg = np.mean(img[xr, yr])
    rmeans[i] = avg

print(rmeans)
plt.plot(rvals, rmeans)
plt.grid()
plt.show()
