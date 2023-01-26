emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}


loves = {'я люблю':['шоколад','торт'],
         'я не люблю':['рыбу','мясо']}
{'вася':'123',
 'поля':'qwerty'}

for keys,values in loves.items():
	for products in values:
		print(keys+' '+products)


[keys+' '+products for keys,values in loves.items() for products in values]

a = [1,2,4,5,5,4,3,1]
print(sorted(i for i in a))
print(*sorted(i for i in a))
print(*sorted(i for i in a),sep = '\n')