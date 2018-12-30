def main():
    print("I am main function")


# 这句话的意思是即可以让当前模块可执行,也可以让该模块被其他模块导入
# 运行当前模块的时候__name__等于__main__
# 被导入的时候,__name__等于文件名称
if __name__ == '__main__':
    main()
