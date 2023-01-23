dict = {x:x**2 for x in range(0,5)}
print(dict)

dict0 ={x:y for x in "ABC" for y in "XYZ"}
print(dict0)

dict0 = {x: 'Z' for x in 'ABC'}
print(dict0)

dict0 = {}.fromkeys('ABC','Z')
print(dict0)

dict0 = {x: 'Z' for x in 'ABC'}
print(dict0)

dict01 = {x:y for x,y in [('A',0),('B',1),('C',2)]}
print(dict01)

dict1 = {x: [y for y in range(x, x + 3)] for x in range(4)}


dict2 = {x: [y % 2 for y in range(10)] for x in 'ABC'}


dict3 = {'ABCDE'[i]: [i % 2]*5 for i in range(5)}


dict4 = {x: {y: 0 for y in 'XYZ'} for x in 'ABC'}


dict5 = {x: {y: x for y in 'XYZ'} for x in 'ABC'}


dict6 = {x: {y: [z for z in range(z, z+ 2)] for y in 'XYZ'} for x, z in zip('ABC', range(3))}


dict7 = {i: {j**2 % i for j in range(1, 100)} for i in [4, 5, 8, 9]}


dict8 = {x: {y: 3 for y in 'ABCD' if y != x} for x in 'ABCD'}
print(dict8)

dict9 = {x: 1 if x in 'ACE' else 0 for x in 'ABCDEF'}
print(dict9)






