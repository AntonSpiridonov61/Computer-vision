import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from scipy.ndimage import morphology


def counting_object(image, struct):
    erosion = morphology.binary_erosion(image, struct)
    dilation = morphology.binary_dilation(erosion, struct)
    image -= dilation
    return label(dilation).max()

image = np.load("../src/ps.npy")

struct = np.array([
            np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1]]),

            np.array([[1, 1, 0, 0, 1, 1],
                    [1, 1, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]]),

            np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1],
                    [1, 1, 0, 0, 1, 1]]),
                    
            np.array([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]]),

            np.array([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]])
                ], dtype=object)
                
total_obj = 0
for i in range(len(struct)):
    res = counting_object(image, struct[i])
    total_obj += res
    print(f'count objects = {res} for struct \n {struct[i]} \n')

print("total objects =", total_obj)
