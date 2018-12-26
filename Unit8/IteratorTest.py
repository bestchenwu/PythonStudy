# aDict = {'a': 1, 'b': 2}
# for key in aDict:
#     print("key=%s,value=%s" % (key, aDict[key]))

seq = range(6)

list1 = [x for x in seq if x % 2 == 0]
print(list1)
