set0 = {i**2 for i in [1,2,3,4,5,6,7]}
print(set0)

#
#Условие if указывается после объявления цикла и итерируемого объекта:

set1 =  {i for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if 'a' not in i}
print(set1)

#
#Условное выражение if... else... указывается до объявления цикла:

set2 =   {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2']}
print(set2)
#
#
#Конструкции if и if... else... могут быть использованы одновременно:

set1 =  {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if i[1] == 'c'}
print(set1)
#
