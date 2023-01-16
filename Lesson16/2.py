import random

a = [9,2,89,4]

index = random.randint(0,len(a)-1)
rand_num =a[index]
print(rand_num)

print(random.choice(a))