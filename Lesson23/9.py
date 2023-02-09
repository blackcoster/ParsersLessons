import datetime
import time
def func():
    print('ggg')
    # time.sleep(5)
    # print('проснулся')

a = datetime.datetime.now()
func()
b= datetime.datetime.now()
print(b-a)