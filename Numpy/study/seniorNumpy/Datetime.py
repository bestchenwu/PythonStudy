import numpy as np
import datetime

date64 = np.datetime64('2018-02-04 23:10:10')
# print(date64)
# 只取天的方法
dt64 = np.datetime64(date64, 'D')
print(dt64)
# 取后十天、后十分等方法
print("after ten days:", dt64 + 10)
# 取后十分
tenminutes = np.timedelta64(10, 'm')
print("after ten minutes", date64 + tenminutes)
print(np.datetime_as_string(date64))
# 将np的时间对象转换为datetime的时间对象
datetime64 = date64.tolist()
print(datetime64.day)
print(datetime64.month)
