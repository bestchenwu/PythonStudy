import _thread, threading
from time import ctime, sleep

secsArray = [2, 4]


def loop(name, secs):
    print("loop %d start at %s " % (name, ctime()))
    sleep(secs)
    print("loop %d end at %s " % (name, ctime()))


class MyThread(threading.Thread):

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        # 在python3中手工调用函数的方法
        self.func(*self.args)
        # python2中使用的方法
        # apply(self.func,self.args)


def main():
    loop_name_array = []
    threads = []
    for index in range(len(secsArray)):
        loop_name_array.append(index)

    for index in loop_name_array:
        thread = MyThread(loop, (index, secsArray[index]))
        # thread = threading.Thread(target='loop', args=(index, secsArray[index]))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("all jobs done")


if __name__ == '__main__':
    main()
