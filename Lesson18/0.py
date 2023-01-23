list1 =[]
for i in range (1,11):
    list1.append(i)

print(list1)

list2 = [i for i in range (1,11)]
print(list2)
#
list3 = [i**2 for i in range (1,11)]
print(list3)

list4 = [str(i) for i in range (1,11)]
print(list4)
#
list5 = [i for i in input().split(' ')]
print(list5)

list6 = [i for i in range (1,101) if i%2 ==0]
print(list6)

list7 = [i*j for i in range (1,11) for j in [1,2,3]]
print(list7)
list8 = [i*j for i in range (1,11) if i%2==0 for j in [1,2,3] if j!=2 ]
print(list8)

list9 = tuple([i for i in range (1,11)])
print(list9)
