import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import regionprops, label
import sys

def neighbors4(x, y):
    return (x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)

def neighbors8(y, x):
    return (y-1, x), (y-1, x+1), (y, x+1), (y+1, x+1), (y+1, x), (y+1, x-1), (y, x-1), (y-1, x-1)

def get_boundaries(region):
    image = region.image
    pos = np.where(image)
    boundaries = []
    for x, y in zip(*pos):
        for yn, xn in neighbors4(x, y):
            if yn < 0 or yn > image.shape[0] - 1:
                boundaries.append((y, x))
                break
            elif xn < 0 or xn > image.shape[1] - 1:
                boundaries.append((y, x))
                break
            if image[yn, xn] == 0:
                boundaries.append((y, x))
                break
    return boundaries


def chain_algo(region):
    bounds = get_boundaries(region)
    bounds.append(bounds[0])
    dirs = []
    _chain(0, bounds, dirs)
    return dirs


def _chain(i, bounds, dirs):
    y, x = bounds[i]
    del bounds[i]
    for n, (ny, nx) in enumerate(neighbors8(y, x)):
        if (ny, nx) in bounds:
            dirs.append(n)
            _chain(bounds.index((ny, nx)), bounds, dirs)


def curvature(chain):
    result = []
    for i in range(len(chain)):
        if i == len(chain) - 1:
            result.append(chain[i] - chain[0])
        else:
            result.append(chain[i] - chain[i+1])

    for i in range(len(chain)):
        result[i] = result[i] % 8 
    return result


def match(chain1, chain2):
    print(chain1, chain2)
    if len(chain1) != len(chain2):
        return False
    for i in range(len(chain1)):
        new_chain = chain1[i:] + chain1[:i]
        if chain2 == new_chain:
            return True

    return False


img = np.load("practices/source/similar.npy")

image = np.zeros((30, 30))

image[10:14, 10:12] = 1
image[15:17, 15:19] = 1
labeled = label(img)
region = regionprops(labeled)

chain1 = curvature(chain_algo(region[0]))
chain2 = curvature(chain_algo(region[1]))

print(match(chain1, chain2))

plt.imshow(image)
plt.show()