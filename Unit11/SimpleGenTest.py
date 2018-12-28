# def simpleGen():
#     yield 1
#     yield '2->punch!'
#
#
# myG = simpleGen()
# # next函数在python3中被提升为全局函数
# print(next(myG))
# print(next(myG))

from random import randint


def listGenerator(aList):
    # 注意list每次弹出元素后,size都会变小
    while len(aList) > 0:
        index = randint(0, len(aList))
        try:
            item = aList.pop(index)
            yield item
        except IndexError as e:
            print("out of index:%d " % index)
            break


aList = [1, 2, 3]
lg = listGenerator(aList)
for a in lg:
    print(a)


# def counter(start_at=0):
#     count = start_at
#     while True:
#         val = (yield count) if val is not None:
#         count = val
#     else:
#         count += 1

