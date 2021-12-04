import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.measure import regionprops, label
import math


def get_colors(hsv_image):
    colors = []
    dist = 0
    start_index = 0

    unique_vals = np.unique(hsv_image[:, :, 0])
    epsilon = np.diff(unique_vals).mean()
    
    for i in range(1, unique_vals.shape[0]):
        d = abs(unique_vals[i] - unique_vals[i - 1])
        if abs(dist - d) > epsilon:
            dist = 0
            colors.append(unique_vals[start_index:i].mean() * 360)
            start_index = i    
    colors.append(unique_vals[start_index:].mean() * 360)
    return colors

def count_figures(region, diff):
    center_row, center_col = map(int, region.centroid)
    color_figures = hsv_image[center_row, center_col, 0] * 360
    color_figures = math.trunc(color_figures)

    if colors[0] - diff < color_figures < colors[0] + diff:
        return 'red'
    if colors[1] - diff <  color_figures < colors[1] + diff:
        return 'yellow'
    if colors[2] - diff <  color_figures < colors[2] + diff:
        return 'green'
    if colors[3] - diff <  color_figures < colors[3] + diff:
        return 'turquoise'
    if colors[4] - diff <  color_figures < colors[4] + diff:
        return 'blue'
    if colors[5] - diff <  color_figures < colors[5] + diff:
        return 'purple'
    return 'red'


image = plt.imread('count-figers-color_and_shape/balls_and_rects.png')
hsv_image = color.rgb2hsv(image)

binary = np.sum(image, 2)
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled)

colors = get_colors(hsv_image)[1:]

figures_rect = dict()
figures_circle = dict()

diff = 20

for region in regions:
    res = count_figures(region, diff)
    if np.all(region.image):
        if res in figures_rect:
            figures_rect[res] += 1
        else:
            figures_rect[res] = 1
    else:
        if res in figures_circle:
            figures_circle[res] += 1
        else:
            figures_circle[res] = 1

print('Rect', figures_rect)
print('Circle', figures_circle)
print('Total', labeled.max())
