import re


# match是匹配模式。正则表达式匹配共分为匹配和搜索两种模式
# match(pattern, string, flags=0) 第一个参数表示模式,第二个参数表示要匹配的字符串
# aString = re.match('foo', 'foo')
# aString = re.match('foo', 'seafood')
# if aString is not None:
#     print("aString=%s" % aString.group())
#
# bString = re.search('foo', 'seafood')
# if bString is not None:
#     print("bString=%s" % bString.group())


def matchTest(pattern, string):
    result = re.match(pattern, string)
    if result is not None:
        return result.group()
    else:
        return None


# 第一个匹配3 14之间任意一个字符
patt314 = '3.14'
# 第二个只匹配3.14字符串
pi_patt = '3\.14'
# print(matchTest(patt314, '3.14'))
# print(matchTest(pi_patt, '3.14'))
# print(matchTest(patt314, '3014'))
# c2do匹配测试
# print(matchTest('[cr][23][de][op]', 'c2do'))
# \w 表示任意字母或者数字
# print(matchTest('\w+@\w+\.com', 'hah@test.com'))
# print(matchTest('\w+@\w+\.(\w+\.)?com', 'hah@test.ff.com'))
# result = re.match('(\w+)-(\d+)', 'abc-123')
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# 返回所有匹配的列表
result = re.findall('car','car in car not tar but car')
print(result)