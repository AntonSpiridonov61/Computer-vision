import matplotlib.pyplot as plt
import os
from skimage.color import rgb2gray
from skimage import filters
from skimage.measure import regionprops, label

PATH = 'pencils/source/'
cnt_pencils = 0

for item in os.listdir(PATH):
    image = plt.imread(PATH + item)[20:-40, 20:-100]
    
    gray = rgb2gray(image)
    thresh = filters.threshold_isodata(gray)
    binary = gray.copy() <= thresh
    labeled = label(binary)
    regions = regionprops(labeled)
    temp = []
    for region in regions:
        temp.append(region.major_axis_length)
        try:
            max_el = max(temp)
            if region.eccentricity > 0.99 and max_el == region.major_axis_length:
                cnt_pencils += 1
                temp.remove(max_el)
        except ZeroDivisionError:
            pass

print(f'All pencils = {cnt_pencils}')
