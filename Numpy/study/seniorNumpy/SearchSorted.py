import numpy as np

array = np.arange(10)
index = np.searchsorted(array, 5, side='right')
print(index)
