import numpy as np
from collections import Counter

for i in range(1, 7):
    with open(f'source/figure{i}.txt') as file:
        size_mm = float(file.readline())
        file.readline()
        image = np.loadtxt(file)
        index_ones = np.nonzero(image[:])
        count_elem = Counter(index_ones[0])
        if count_elem:
            cnt_pix = max([elem for elem in count_elem.values()])
            print(f'figure{i} nominal_resolution: {size_mm / cnt_pix}')
        else:
            print(f'figure{i} Image not found')
