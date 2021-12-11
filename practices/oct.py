import numpy as np
import matplotlib.pyplot as plt
from skimage import draw
from skimage.filters import gaussian, threshold_otsu


def hist(array):
    h = np.zeros(256)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            h[array[i, j]] += 1
    return h


def find_extrema(array):
    extrema = []
    for i in range(1, len(array) - 1, 1):
        if array[i - 1] < array[i] > array[i + 1]:
            extrema.append(i)
    return extrema


image = np.zeros((1000, 1000), dtype="uint8")
image[:] = np.random.randint(20, 75, size=image.shape)

rr, cc = draw.disk((500, 500), 90)
image[rr, cc] = np.random.randint(100, 200, size=len(rr))

rr, cc = draw.disk((100, 100), 90)
image[rr, cc] = np.random.randint(220, 240, size=len(rr))

image = (gaussian(image, sigma=1) * 255).astype("uint8")

threshold = 90
b = image.copy()
b[b<threshold] = 0
b[b > 0] = 1

h = hist(image)
extrema = find_extrema(h)

plt.subplot(131)
plt.imshow(image)
plt.subplot(132)
plt.plot(h)

extrema_vals = h[extrema]
s = np.std(extrema_vals)
new_extrema = []
for i in range(len(extrema_vals)):
    if extrema_vals[i] > 0.5 * s:
        new_extrema.append(extrema[i])

auto_threshold = np.mean(new_extrema)

print(threshold_otsu(image))

plt.plot(new_extrema, h[new_extrema] ,"o")
plt.plot(np.diff(h), "r")
plt.subplot(133)
plt.imshow(b)
plt.show()
