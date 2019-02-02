import numpy as np

# array = np.array([20, 18, 14, 17, 20, 21, 15])
# max_value = np.max(array)
# min_value = np.min(array)
# print(max_value-min_value)

prices = np.full(100, fill_value=np.nan)
prices[[0, 25, 60, -1]] = [80., 30., 75., 50.]
x = np.arange(len(prices))
is_valid = ~np.isnan(prices)
prices = np.interp(x=x, xp=x[is_valid], fp=prices[is_valid])
#print(prices)
prices += np.random.randn(len(prices)) * 2
