import threading
import time

class Crawler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.done = False

    def isDone(self):
        return self.done

    def run(self):
        time.sleep(5)
        self.done = True
        raise Exception ('what happened')

t = Crawler()
t.start()
while True:
    time.sleep(1)
    if t.isDone():
        print('DONE')
        break
    if not t.is_alive():
        t = Crawler()
        t.start()