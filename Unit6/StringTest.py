import string
# aString="abcde"
# print(aString[0])
# print(aString[:3])

#print(string.ascii_letters)
#print(string.ascii_uppercase)

# str='%s %s' % ('spanish','china')
# print(str)
#python3中的join表示循环第二个元素,将第一个元素嵌入其中
# str1='sweet'.join('haha')
# print(str1)
# str3='hello'+u' '+'world'
# print(str3)
# str4='ab'
# print(str4*3)
# print('%.2f' % 35.2324)
# from string import Template
# str=Template("the ${language} is ${code}")
# print(str.substitute(language="python",code="print"))
# print(str.safe_substitute(language="python"))
str='abc'
#获得字符串的下标和每个位置的值
# for index,t in enumerate(str):
#     print(index,t)
##把元组里的每个元素提取出来
# a,b=('abc','def')
# abZip=zip(a,b)
# for item in abZip:
#     print(item)
quest='what is favor color'
##在长度40的范围内，让quest居中
print(quest.center(40,'-'))
str1='bc'
index = str.find(str1)
print(index)