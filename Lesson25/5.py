try:
    f = open('1.txt')
except:
    print('нету')
ints = []

try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print('Это не число')
except Exception:
    print('Что это вообще такое?')
else:
    print('Все хорошо')

finally:
    f.close()
    print('я закрыл файл')


