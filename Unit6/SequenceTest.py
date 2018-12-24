##从左往右数,坐标依次为0,1,2,3,4
##从右往左数,坐标依次为-1,-2,-3,-4,-5
##进行字符串截断的时候，只能从左往右截断，不能从右往左
str="abcde"
# print(str[::-1])
# print(str[:2])
# print(str[2:4])
# print(str[3:8])
# for index in [None]+[x for x in range(-1,-len(str),-1)]:
#     print(str[:index])

#print(str[8])
print(str[-3:-1])
