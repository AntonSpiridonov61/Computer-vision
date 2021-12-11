import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label

def math(a, masks):
    for mask in masks:
        if np.all(a == mask):
            return True
        return False

def euler(labeled, label):
    pxs = np.where(labeled == label)
    e = 0
    i = 0
    for y in range(pxs[0].min() - 1, pxs[0].max() + 1):
        for x in range(pxs[1].min() - 1, pxs[1].max() + 1):
            sub = image[y:y+2, x:x+2]
            if math(sub, [exter_mask]):
                e += 1
            elif math(sub, [inter_mask]):
                i += 1
    return e - i

image = np.load("../src/holes.npy")

labeled = label(image)

exter_mask = np.array([[0, 0], 
                        [0, 1]])
inter_mask = np.array([[1, 1], 
                        [1, 0]])

for i in range(1, 10):
    print(i, '=', 1 - euler(labeled, i))

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(labeled)
plt.show()
