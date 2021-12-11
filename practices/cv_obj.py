import numpy as np
import matplotlib.pyplot as plt

def area(LB, label=1):
    pxs = np.where(LB == label)
    return len(pxs[0])

def centroid(LB, label=1):
    pxs = np.where(LB == label)
    cy = np.mean(pxs[0])
    cx = np.mean(pxs[1])
    return cy, cx

def neighbors4(y, x):
    return (y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)

def get_boundaries(LB, label=1):
    pxs = np.where(LB == label)
    boundaries = []
    for y, x in zip(*pxs):
        for yn, xn in neighbors4(y, x):
            if yn < 0 or yn > LB.shape[0] - 1:
                boundaries.append((y, x))
                break
            elif xn < 0 or xn > LB.shape[1] - 1:
                boundaries.append((y, x))
                break
            elif LB[yn, xn] != label:
                boundaries.append((y, x))
                break
    return boundaries

def draw_boundaries(LB, label=1):
    BB = np.zeros_like(LB)
    pos = np.where(LB == label)
    BB[pos] = LB[pos]
    for y, x in get_boundaries(BB, label):
        BB[y, x] = label + 1
    return BB

# def circularity(LB, label=1):
#     ...

def distance(px1, px2):
    return ((px1[0] - px2[0]) ** 2 + (px1[1] - px2[1]) ** 2) ** 0.5

def radial_distance(LB, label=1):
    r, c = centroid(LB, label)
    boundaries = get_boundaries(LB, label)
    K = len(boundaries)
    rd = 0
    for rk, ck in boundaries:
        rd += distance((r, c), (rk, ck))
    return rd / K

def std_radial(LB, label=1):
    r, c = centroid(LB, label)
    rd = radial_distance(LB, label)
    boundaries = get_boundaries(LB, label)
    K = len(boundaries)
    sr = 0
    for rk, ck in boundaries:
        sr += (distance((r, c), (rk, ck)) - rd) ** 2
    return (sr / K) ** 0.5

def circularity_std(LB, label=1):
    return radial_distance(LB, label) / std_radial(LB, label)


LB = np.zeros((16, 16))
LB[4:, :4] = 2

LB[3:10, 8:] = 1
LB[[3, 4, 3],[8, 8, 9]] = 0
LB[[8, 9, 9],[8, 8, 9]] = 0
LB[[3, 4, 3],[-2, -1, -1]] = 0
LB[[9, 8, 9],[-2, -1, -1]] = 0

LB[12:-1, 6:9] = 3

print(area(LB, 1))
print(area(LB, 2))
print(area(LB, 3))

print(circularity_std(LB, 1))
print(circularity_std(LB, 2))
print(circularity_std(LB, 3))

# BB = draw_boundaries(LB, 1)
# plt.subplot(121)
# plt.imshow(BB)
# plt.show()

# plt.subplot(122)
plt.imshow(LB)
plt.show()