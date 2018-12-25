import string

str = input("please input a validator:")
alphaWords = string.ascii_letters + "_"
alphaAndNumbers = alphaWords + string.digits
flag = 1
if str.__len__() < 2:
    print("str length must be larger than 2")
    flag = 0
else:
    firstWord = str[0]
    if (firstWord not in alphaWords):
        print("the first word must be alphaWord")
        flag = 0
    else:
        otherWords = str[1:]
        for char in otherWords:
            if (char not in alphaAndNumbers):
                print("other word must be alpha or number")
                flag = 0
                break
if (flag == 1):
    print("the validator is valid")
