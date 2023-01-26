numbers = [1,2,3,4]
result = (x*x for x in numbers)
# result1 = [x*x for x in numbers]
print(next(result))
print(next(result))
print(next(result))
print(next(result))

for num in result:
    print(num)

# print(next(result))
# print(result1)