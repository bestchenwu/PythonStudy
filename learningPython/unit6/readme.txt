本章描述python的序列格式的对象

0   1  2   3
a   b  c   d
-4 -3 -2   -1

序列操作函数
seq[i] 取第几个元素
seq[i:j] 取[i,j)区间的元素(seq[i:j:-1] 表示倒序取元素)
特殊情况seq[::-1]等于将seq反转
seq * i  将seq重复几遍
seq1+seq2  将两个序列联合
obj (not) in seq 判断某个对象是否在序列中