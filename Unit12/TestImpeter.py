import sys

# sys.path.append('/data/StudySpace/PythonStudy')
# from Unit12.Impeter import foo, show
#
# show()
# foo = 333
# print("foo=%d " % foo)
# show()


# 如果想改变模块里的属性，需要加上属性的命名空间
print(sys.path)
# 相对导入
import Unit12.Impeter as Impeter
# 如果前面加一个_则表示不导入这个模块
import tkinter._dialog
# from . import Impeter
Impeter.show()
Impeter.foo = 333
Impeter.show()

# from __future__ import division

