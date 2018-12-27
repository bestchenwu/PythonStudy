import os

for temp in ('/temp', r'/data/problem/temp'):
    if os.path.isdir(temp):
        break
    else:
        print("not a temp director,name=%s" % temp)
        pass

os.chdir(temp)
# 先输出目前所有的目录
print("current path is %s" % os.getcwd())
dirs = os.listdir(temp)
print(dirs)
if not os.path.exists("example"):
    os.mkdir("example")
os.chdir("example")
print("current path is %s" % os.getcwd())
# 创建写文件
file1 = open('exampleFile', 'w+')
file1.write('hello')
file1.write(os.linesep)
file1.write('world')
dirs = os.listdir(os.curdir)
print(dirs)
