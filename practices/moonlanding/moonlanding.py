import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('moonlanding.png')
ft = np.fft.fft2(image)
cft = np.fft.fftshift(ft)
ft[50:-50, :] = 0
ft[:, 50:-50] = 0

rests = np.fft.ifft2(ft)

plt.figure()
plt.imshow(np.log(np.abs(cft)))
plt.figure()
plt.imshow(np.abs(rests), cmap='gray')
plt.show()