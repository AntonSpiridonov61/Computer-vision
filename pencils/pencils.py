import matplotlib.pyplot as plt
import os
from skimage.color import rgb2gray
from skimage import filters, morphology
from skimage.measure import regionprops, label

PATH = 'pencils/source/'
cnt_pencils = 0
major_list = []


for item in os.listdir(PATH):
    image = plt.imread(PATH + item)[20:-40, 20:-100]
    
    gray = rgb2gray(image)
    thresh = filters.threshold_isodata(gray)
    binary = gray <= thresh
    binary = morphology.remove_small_objects(binary)
    binary = morphology.remove_small_holes(binary)
    labeled = label(binary)
    regions = regionprops(labeled)
    for region in regions:
        length = region.major_axis_length
        major_list.append(length)

max_major = max(major_list)
for i in major_list:
    if i / max_major > 0.8:
        cnt_pencils += 1

print(f'All pencils = {cnt_pencils}')
