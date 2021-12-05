import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.measure import regionprops, label


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

def get_border_colors(colors):
    border_colors = []
    for i in range(len(colors)):
        if i == len(colors) - 1:
            border_colors.append((colors[i] + 360.0) / 2)
        else:  
            border_colors.append((colors[i] + colors[i + 1]) / 2)
    return border_colors

def get_color_figure(region):
    center_row, center_col = map(int, region.centroid)
    color_figures = hsv_image[center_row, center_col, 0] * 360

    if color_figures < border_colors[0]:
        return 'red'
    if color_figures < border_colors[1]:
        return 'yellow'
    if color_figures < border_colors[2]:
        return 'green'
    if color_figures < border_colors[3]:
        return 'turquoise'
    if color_figures < border_colors[4]:
        return 'blue'
    if color_figures < border_colors[5]:
        return 'purple'
    return 'red'


image = plt.imread('count-figers-color_and_shape/balls_and_rects.png')
hsv_image = color.rgb2hsv(image)

binary = np.sum(image, 2)
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled)

colors = get_colors(hsv_image)[1:]
border_colors = get_border_colors(colors)

figures_rect = dict()
figures_circle = dict()

for region in regions:
    color_figure = get_color_figure(region)
    if np.all(region.image):
        if color_figure in figures_rect:
            figures_rect[color_figure] += 1
        else:
            figures_rect[color_figure] = 1
    else:
        if color_figure in figures_circle:
            figures_circle[color_figure] += 1
        else:
            figures_circle[color_figure] = 1

print('Rect', figures_rect)
print('Circle', figures_circle)
print('Total', labeled.max())
