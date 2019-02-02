array = [20, 18, 14, 17, 20, 21, 15]


def find_max_profit():
    min = array[0]
    max = array[1]
    for i in array:
        if i < min:
            min = i
        elif i > max:
            max = i
        else:
            pass
    return (min, max)


tuple1 = find_max_profit()
print(tuple1[1] - tuple1[0])
