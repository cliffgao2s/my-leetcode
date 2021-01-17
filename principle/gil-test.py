import threading
import time

#lock = threading.Lock()

# 有了GIL全局锁，线程间访问全局变量还是需要同步
total = 0
def add():
    global total
    #lock.acquire()
    for i in range(1000000):
        total += 1
    #lock.release()

def desc():
    global total
    #lock.acquire()
    for i in range(1000000):
        total -= 1
    #lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)