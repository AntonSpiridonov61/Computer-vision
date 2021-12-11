import numpy as np
import matplotlib.pyplot as plt

def check(image, y, x):
    if not 0 <= x < image.shape[1]:
        return False
    if not 0 <= y < image.shape[0]:
        return False
    if image[y,x] !=0:
        return True
    return False

def neighbours2(image,y,x):
    left = y, x-1
    top = y-1,x

    if not check(image, *left):
        left = None
    if not check(image, *top):
        top = None

    return left,top

def find(label,linked):
    j = int(label)
    while linked[j] != 0:
        j = linked[j]
    return j

def union(label1,label2,linked):
    j = find(label1,linked)
    k = find(label2,linked)
    if j != k:
        linked[k] = j
    


def two_pass_labeling(b_image):
    labeled = np.zeros_like(b_image)
    label = 1
    linked = np.zeros(len(b_image), dtype='uint')

    for y in range(b_image.shape[0]):
        for x in range(b_image.shape[1]):
            if b_image[y,x] != 0:
                ns = neighbours2(b_image,y,x)
                if ns[0] is None and ns[1] is None:
                    m = label
                    label += 1
                else:
                    lbs = [labeled[i] for i in ns if i is not None]
                    m = min(lbs)
                labeled[y,x] = m

                for n in ns:
                    if n is not None:
                        lb = labeled[n]
                        if lb != m:
                            union(m, lb, linked)

    labs = []
    
    for y in range(b_image.shape[0]):
        for x in range(b_image.shape[1]):
            if b_image[y,x] != 0:
                new_label = find(labeled[y,x],linked)
                
                if new_label != labeled[y,x]:
                    labeled[y,x] = new_label                    
                if new_label not in labs:
                    labs.append(new_label)
                if labeled[y,x] in labs:
                    labeled[y,x] = labs.index(new_label) + 1

    return labeled

def area(LB, label=1):
    pxs = np.where(LB == label)
    return len(pxs[0])



coins = {1: 0, 2: 0, 5: 0, 10: 0}

image = np.load("src/coins.npy").astype('uint')

image1 = two_pass_labeling(image)
for i in range(1, 51):
    area_coin = area(image1, i)
    if area_coin == 69: coins[1] += 1
    if area_coin == 145: coins[2] += 1
    if area_coin == 305: coins[5] += 1
    if area_coin == 609: coins[10] += 1

print(coins)

summary = 0
for index, count in coins.items():
    summary += index * count
print(summary)

plt.imshow(image1)
plt.show()