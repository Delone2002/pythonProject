#!/usr/bin/python3

import numpy as np

array = np.random.randint(-100, 100, (3, 3))
print(f'Массив\n{array}')
print(f'Транспонированный массив\n{array.transpose()}')