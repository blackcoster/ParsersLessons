import threading
import time


def crawler(url):
    data = threading.local()
    data.visited = []

t = threading.Thread(target=crawler,args=('https://en.wikipedia.org/wiki/Roger_Leenhardt'))
t.start()

while True:
    time.sleep(1)
    if not t.isAlive():
        t = threading.Thread(target=crawler).start()