import matplotlib.pyplot as plt
from wavelengthtorgb import wavelength_to_rgb
import numpy as np

# Hydrogen
plt.figure(1)
plt.title('Vesiniku spektrijooned')
plt.xlabel('Lainepikkus (nm)')
plt.xticks([410, 434, 486, 656])
frame1 = plt.gca()
frame1.axes.get_yaxis().set_visible(False)
frame1.set_xlim(300, 800)

rgb = wavelength_to_rgb(410, gamma=0.8)
plt.axvline(x=410, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(434, gamma=0.8)
plt.axvline(x=434, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(486, gamma=0.8)
plt.axvline(x=486, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(656, gamma=0.8)
plt.axvline(x=656, linewidth=2, color=np.array(rgb)/max(rgb))

# Mercury
plt.figure(2)
plt.title('Elavhõbeda spektrijooned')
plt.xlabel('Lainepikkus (nm)')
plt.xticks([404, 502, 546, 579])
frame1 = plt.gca()
frame1.axes.get_yaxis().set_visible(False)
frame1.set_xlim(300, 800)

rgb = wavelength_to_rgb(404, gamma=0.8)
plt.axvline(x=404, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(407, gamma=0.8)
plt.axvline(x=407, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(502, gamma=0.8)
plt.axvline(x=502, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(546, gamma=0.8)
plt.axvline(x=546, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(577, gamma=0.8)
plt.axvline(x=577, linewidth=2, color=np.array(rgb)/max(rgb))
rgb = wavelength_to_rgb(579, gamma=0.8)
plt.axvline(x=579, linewidth=2, color=np.array(rgb)/max(rgb))

plt.show()
