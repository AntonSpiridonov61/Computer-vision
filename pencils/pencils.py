import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.color import rgb2gray
from skimage import filters
from skimage.measure import regionprops, label

# from skimage.filters import try_all_threshold





PATH = 'pencils/source/'

for item in os.listdir(PATH):
    image = plt.imread(PATH + item)[10:-30, 10:-30]
    gray = rgb2gray(image)
    thresh = filters.threshold_isodata(gray)
    binary = gray < thresh

    labeled = label(binary)
    plt.imshow(labeled)
    regions = regionprops(labeled)
    for region in regions:
        if region.area > 20000:
            plt.imshow(region.image, cmap='gray')
            plt.show()

    # fig, ax = try_all_threshold(gray, figsize=(10, 8), verbose=False)
    # plt.show()


