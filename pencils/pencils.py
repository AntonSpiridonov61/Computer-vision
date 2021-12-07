import matplotlib.pyplot as plt
import os
from skimage.color import rgb2gray
from skimage import filters
from skimage.measure import regionprops, label

PATH = 'pencils/source/'
cnt_pencils = 0

for item in os.listdir(PATH):
    image = plt.imread(PATH + item)[20:-40, 20:-40]
    
    gray = rgb2gray(image)
    thresh = filters.threshold_isodata(gray)
    binary = gray.copy() <= thresh
    labeled = label(binary)
    regions = regionprops(labeled)
    temp = []
    for region in regions:
       
        if region.area > 2000.0 and region.major_axis_length / region.minor_axis_length > 19.0:
            cnt_pencils += 1

print(f'All pencils = {cnt_pencils}')
