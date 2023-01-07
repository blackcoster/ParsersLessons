import json
dict_person={}
while len(dict_person)!=3:
    name = input("Введите имя ")
    age = input('Введите возраст ')
    if name not in dict_person:
        dict_person[name] = age
    else:
        print('имя есть')

with open('task.txt','w',encoding ='utf-8') as file:
    file.write(json.dumps(dict_person,ensure_ascii=False, indent=4))


