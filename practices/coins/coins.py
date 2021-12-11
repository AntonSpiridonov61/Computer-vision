import numpy as np
import matplotlib.pyplot as plt
from skimage import draw
from skimage.filters import (gaussian, threshold_otsu, threshold_local, threshold_yen, threshold_li)


def hist(array):
    h = np.zeros(256)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            h[array[i, j]] += 1
    return h

image = plt.imread("coins.jpg")
gray = np.mean(image, 2).astype("uint8")

mean_row = np.mean(gray, 0)
gray = np.divide(gray, mean_row)

th1 = gray.copy() > threshold_local(gray, 101)
th2 = gray.copy() > threshold_otsu(gray)
th3 = gray.copy() > threshold_li(gray)
th4 = gray.copy() > threshold_yen(gray)

plt.subplot(151)
plt.imshow(gray)
plt.subplot(152)
plt.imshow(th1)
plt.subplot(153)
plt.imshow(th2)
plt.subplot(154)
plt.imshow(th3)
plt.subplot(155)
plt.imshow(th4)
plt.show()