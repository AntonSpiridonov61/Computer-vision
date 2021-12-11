import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage.measure import regionprops, label

image = plt.imread("../src/lama_on_moon.png")[21: -40, 45: -20]
image = np.mean(image, 2)

sobel = np.abs(filters.sobel(image))
threshold = filters.threshold_otsu(sobel)
sobel[sobel < threshold] = 0
sobel[sobel > 0] = 1

region = None
labeled = label(sobel)
for r in regionprops(labeled):
    if region is None or region.perimeter < r.perimeter:
        region = r

labeled[labeled != region.label] = 0

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(labeled)
plt.show()