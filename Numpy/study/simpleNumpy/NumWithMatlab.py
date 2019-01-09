import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, np.pi * 2, 10)
b = np.sin(a)
print(a)
print(b)
plt.plot(a, b)  # a作为横坐标,b作为纵坐标
# mask = b >= 0 # 这是布尔表达式(表示取符合条件的值)
# plt.plot(a[mask], b[mask], 'bo') # 这样就取出了一半的值
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')  # 这样就只取出了上集合的一半值
plt.show()
