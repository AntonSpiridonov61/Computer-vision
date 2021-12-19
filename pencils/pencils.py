import matplotlib.pyplot as plt
import os
from skimage.color import rgb2gray
from skimage import filters
from skimage.measure import regionprops, label
import numpy as np

PATH = 'pencils/source/'
cnt_pencils = 0
temp_minor = []

for item in os.listdir(PATH):
    image = plt.imread(PATH + item)[20:-40, 20:-100]
    
    gray = rgb2gray(image)
    thresh = filters.threshold_isodata(gray)
    binary = gray.copy() <= thresh
    labeled = label(binary)
    regions = regionprops(labeled)
    temp_major = []
    
    for region in regions:
        temp_major.append(region.major_axis_length)
        # temp_minor.append(region.minor_axis_length)

    # temp_major.sort()
    max_diff = 0
    idx = len(temp_major)
    for i in range(0, len(temp_major)-1):
        if (temp_major[i+1] - temp_major[i]) > max_diff:
            max_diff = temp_major[i+1] - temp_major[i]
            idx = i + 1
    temp_minor.append(max_diff)
    # print(temp_major[idx:len(temp_major)])

print(temp_minor)
print(np.array(temp_minor).mean())
print(f'All pencils = {cnt_pencils}')
