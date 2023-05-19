import _thread
import time


def print_time(threadName,delay,iterations):
    start = int(time.time())
    for i in range(iterations):
        time.sleep(delay)
        seconds = int(time.time() - start)
        print(f'Поток {threadName} прошло {seconds}')

try:
    _thread.start_new_thread(print_time,('Thread1',3,33))
    _thread.start_new_thread(print_time,('Thread2',5,20))
    _thread.start_new_thread(print_time,('Thread3',1,20))
except:
    print('ошибка с потоками')

while 1:
    pass