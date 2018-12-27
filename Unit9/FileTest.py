import os
file_object = open('haha.txt', mode='r+', buffering=-1)
# for line in file_object.readlines():
#     # python默认把换行符号也会读出来，所以需要用line.strip来去掉换行符
#     # 同理在写入的时候，需要手工加上换行符
#     print("line=%s" % line.strip())

newContent = ['jack', 'marry']
for content in newContent:
    # os支持的行分割符
    file_object.write(os.linesep)
    file_object.write(content)
    print(file_object.tell())

file_object.close()

