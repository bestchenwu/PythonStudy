file = None
try:
    file = open('test.txt')
# python2的表达方式是IOError,e
except IOError as ioerror:
    # 查看python error的属性
    print(ioerror)
    print(ioerror.__class__)
    print(ioerror.__doc__)
    # print('none.txt not found')
# 这样是表示多个异常
except (ValueError, TypeError):
    pass
else:
    print("first line:%s" % file.readline())
# python3中不支持裸except
# except:
finally:
    if file:
        file.close()
