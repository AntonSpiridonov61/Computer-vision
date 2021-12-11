import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face
from scipy.ndimage.morphology import binary_dilation


def translation(B, vector):
    translated = np.zeros_like(B)
    for y in range(translated.shape[0]):
        for x in range(translated.shape[1]):
            new_y = y + vector[0]
            new_x = x + vector[1]
            if new_x < 0 or new_y < 0:
                continue
            if new_x >= B.shape[0] or new_y >= B.shape[1]:
                continue
            translated[new_y, new_x] = B[y, x]
    return translated

def dilation(arr, mask=np.ones((3, 3))):
  result = np.zeros_like(arr)
  for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
          if arr[y, x] != 0:
            r = np.logical_or(arr[y-1: y+2, x-1: x+2], mask)
            result[y-1: y+2, x-1:x+2] = r
  return result

def erosion(arr, mask=np.ones((3, 3))):
  result = np.zeros_like(arr)
  for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
          r = arr[y-1: y+2, x-1: x+2]
          if np.all(r == mask):
            result[y, x] = 1
  return result

def closing(arr, mask=np.ones((3, 3))):
  return erosion(dilation(arr, mask), mask)

def opening(arr, mask=np.ones((3, 3))):
  return dilation(erosion(arr, mask), mask)


cross = np.ones((3, 3))
cross[0, 0] = 0
cross[-1, 0] = 0
cross[0, -1] = 0
cross[-1, -1] = 0

arr = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]])

image = face(gray=True)

# translated = translation(image, (50, 50))

res = opening(arr)

plt.subplot(121)
plt.imshow(res)
plt.subplot(122)
plt.imshow(arr)
plt.show()
