try:
    file = open('')
except:
    import sys

    exec_tuple = sys.exc_info()
    # print(exec_tuple)
    for eachItem in exec_tuple:
        print(eachItem)
