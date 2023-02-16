import time
from functools import cache


@cache
def func(n):
    result = 0
    for i in range(n):
        result+=i
        # result = result+i
    return result

start_time = time.time()
print(func(100_000_000))
end_time = time.time()
print(end_time-start_time)

print('\n')
start_time1 = time.time()
print(func(100_000_000))
end_time1 = time.time()
print(end_time1-start_time1)

# start_time2 = time.time()
# print(func(100_000_001))
# end_time2 = time.time()
# print(end_time2-start_time2)