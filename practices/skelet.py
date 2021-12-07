import matplotlib.pyplot as plt
import numpy as np
from skimage import draw
import cv2

image = np.zeros((200, 200), dtype='uint8')

r, c = draw.rectangle((10, 50), (190, 80))
image[r, c] = 1

r, c = draw.rectangle((10, 120), (190, 150))
image[r, c] = 1

r, c = draw.rectangle((75, 80), (105, 120))
image[r, c] = 1

skel = np.zeros(image)
elem = cv2.getStructuringElement(cv2.MORP_CROSS, (3, 3))

while True:
    pass

plt.figure()
plt.imshow(image)
plt.show()