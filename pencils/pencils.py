import matplotlib.pyplot as plt
import numpy as np
import os

files = os.listdir()
print(files)
for item in os.walk('pencils/source/'):
    print(item)
    image = plt.imread(item)
    plt.imshow(image)
    plt.show()


# image = plt.imread('source/img (1).jpg')
# plt.imshow(image)
# plt.show()