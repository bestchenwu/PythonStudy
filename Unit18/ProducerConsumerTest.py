import threading
from time import ctime, sleep
from random import randint
from queue import Queue


def write(queue):
    # print("Producer produce start:%s" % ctime())
    value = randint(1, 99)
    queue.put(value)
    print("Producer put value %d " % value)
    # print("Producer produce end:%s" % ctime())
    sleep(randint(1, 3))


def write_q(count, queue):
    for i in range(count):
        write(queue)


def get(queue):
    # print("Consumer consume start:%s" % ctime())
    value = queue.get()
    print("consumer consume value %d " % value)
    # print("Consumer consume end:%s" % ctime())
    sleep(randint(1, 3))


def get_q(count, queue):
    for i in range(count):
        get(queue)


def main():
    queue = Queue(30)
    # todo:这里不合理的地方是创建线程的时候指定的函数必须接受一个参数列表，而不能是queue
    consumer_thread = threading.Thread(target=get_q, name="consumerThread", args=(5, queue))
    producer_thread = threading.Thread(target=write_q, name="producerThread", args=(5, queue))
    consumer_thread.start()
    producer_thread.start()
    consumer_thread.join()
    consumer_thread.join()


if __name__ == '__main__':
    main()
