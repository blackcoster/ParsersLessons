# tuple1 = tuple([i for i in range(5,26)])
# print(tuple1[-5:])

print([int(i) for i in input().split(',') if int(i)%3==0 or int(i)%5==0])