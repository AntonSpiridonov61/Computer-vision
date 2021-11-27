import matplotlib.pyplot as plt
import os
from skimage.color import rgb2gray
from skimage import filters
from skimage.measure import regionprops, label

PATH = 'pencils/source/'
cnt_pencils = 0

for item in os.listdir(PATH):
    image = plt.imread(PATH + item)[10:-30, 10:-30]
    
    gray = rgb2gray(image)
    thresh = filters.threshold_otsu(gray)
    binary = gray.copy() <= thresh
    labeled = label(binary)
    regions = regionprops(labeled)

    for region in regions:
        if 2800 < region.major_axis_length < 3200:
            cnt_pencils += 1

print(f'All pencils = {cnt_pencils}')
