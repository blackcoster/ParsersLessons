import threading
import time


def print_time(name, delay, iter):
    start = int(time.time())
    for i in range(iter):
        time.sleep(delay)
        end = int(time.time()) - start
        print(f'{name} {end}')



threading.Thread(target=print_time, args=('PPPP', 3, 33)).start()
threading.Thread(target=print_time, args=('ooooo', 1, 33)).start()
threading.Thread(target=print_time, args=('vvvvv', 5, 33)).start()
