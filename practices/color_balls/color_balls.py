import matplotlib.pyplot as plt
import numpy as np
from skimage import color


def get_colors(hsv):
    arr = np.unique(hsv[:, :, 0])
    return np.diff(arr)

image = plt.imread('balls.png')

image_hsv = color.rgb2hsv(image)
unique_hsv = np.unique(image_hsv[:, :, 0])

print(get_colors(image_hsv))

# plt.subplot(121)
# plt.imshow(image_hsv)
# plt.subplot(122)
plt.plot(unique_hsv, 'o')
plt.plot(np.diff(unique_hsv))
plt.show()