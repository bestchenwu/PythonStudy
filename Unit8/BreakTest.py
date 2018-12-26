num = 5
count = num // 2
while count > 0:
    if num % count == 0:
        print("the bigest count is %d" % count)
        break
    # else:
    #     continue
    count -= 1

