##在python3中使用input
fname=input('input file name:')
print(fname)

try:
    file = open(fname,'r')
except Exception as e:
    print(e)
else:
    for line in file:
        print(line)
    file.close()
