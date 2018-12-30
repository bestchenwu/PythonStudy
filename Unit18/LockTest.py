import _thread, threading
from time import ctime, sleep

secsArray = [2, 4]


def loop(loopName, secs, lock):
    print("loop %d start at %s " % (loopName, ctime()))
    sleep(secs)
    print("loop %d end at %s " % (loopName, ctime()))
    # todo: 这里为什么一直释放不成功呢
    lock.release()


def main():
    loop_name_array = []
    locks = []
    for index in range(len(secsArray)):
        loop_name_array.append(index)
        lock = threading.Lock()
        # lock = _thread.allocate_lock()
        # lock.acquire()
        locks.append(lock)

    for index in loop_name_array:
        currentLock = locks[index]
        if currentLock.acquire():
            _thread.start_new_thread(loop, (index, secsArray[index], currentLock))

    for lock in locks:
        while lock.locked:
            pass

    print("all jobs done")


if __name__ == '__main__':
    main()
