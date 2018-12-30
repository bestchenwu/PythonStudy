# compile有三个参数，分别为要编译的python代码,要存放代码对象的文件名字(通常为空),表明代码对象的类型
# 该类型通常包括:
# eval 可求值的表达式
# single 单一可执行语句
# exec 可执行语句组
compile1 = compile('100+200', '', 'eval')
print(eval(compile1))
