import _thread, threading
from time import ctime, sleep

secsArray = [2, 4]


def loop(loop_name, secs):
    print("loop %d start at %s " % (loop_name, ctime()))
    sleep(secs)
    print("loop %d end at %s " % (loop_name, ctime()))


def main():
    loop_name_array = []
    threads = []
    for index in range(len(secsArray)):
        loop_name_array.append(index)

    for index in loop_name_array:
        thread = threading.Thread(target=loop, args=(index, secsArray[index]))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("all jobs done")


if __name__ == '__main__':
    main()
