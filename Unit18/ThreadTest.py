import _thread
from time import ctime, sleep


def loop0():
    print("loop0 start at %s" % ctime())
    sleep(4)
    print("loop0 end at %s" % ctime())


def loop1():
    print("loop1 start at %s" % ctime())
    sleep(2)
    print("loop1 end at %s" % ctime())


def main():
    # 第一个参数是函数名称,第二个参数是函数的参数,如果函数不需要参数，就传一个空元组
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    # 这里必须要加上sleep的合适睡眠时间(因为当主线程退出的时候，子线程也退出了)
    sleep(10)


if __name__ == '__main__':
    main()
