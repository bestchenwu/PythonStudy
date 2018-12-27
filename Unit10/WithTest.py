# with语句是用于管理上下文对象,执行完成后自动关闭
with open('test.txt') as fileObj:
    for line in fileObj:
        print(line.strip())
