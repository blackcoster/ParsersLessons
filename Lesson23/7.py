import sys
import time
def get_size(func):
   def wrapper(a, b, delay=0):
       result = sys.getsizeof(func(a, b, delay))
       print(f'>> функция  занимает в памяти: {result} байт')
   return wrapper

@get_size
def add_with_delay(a, b, delay=0):
   print('сложить', a, b, delay)
   time.sleep(delay)
   return a * b

print('старт программы')
add_with_delay(10000, 200000)
add_with_delay(10, 20, 1)
print('конец программы')
