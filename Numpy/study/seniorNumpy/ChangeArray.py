import numpy as np

# array = np.arange(10)
# print(array)
# # 将一维数组转换为二维数组
# newArray = array[:, np.newaxis]
# print(newArray.shape)
# print(newArray)
 #bins = [3, 6, 9]
# 循环array,记为data
# 再循环bins,如果满足bins[i]<data<bins[i+1]
# 则返回i,接着再继续循环array
# print(np.digitize(array, bins))
# 当array里低于3的时候以3代替,当大于8的时候以8代替
# print(np.clip(array, 3, 8))

array = np.array([2, 2, 3, 3, 4, 5, 6, 8])
# 返回数组里从1到最大数字(8)的出现频率
print(np.bincount(array))
#返回直方图  分布返回bins[0,i)、bins[i,i+1)、...、bins[length-1,length]的元素个数,
counts, bins = np.histogram(array, [0, 2, 4, 6])
print(counts)
print(bins)
