import numpy as np

def get_indexes_ones(path):
    with open(path) as file:
        file.readline()
        file.readline()
        image = np.loadtxt(file)
        indexes = np.nonzero(image[:])
    return indexes

path1 = 'source/img1.txt'
path2 = 'source/img2.txt'

indexes_img1 = get_indexes_ones(path1)
indexes_img2 = get_indexes_ones(path2)

print((indexes_img1[0] - indexes_img2[0])[0], (indexes_img1[1] - indexes_img2[1])[0])
