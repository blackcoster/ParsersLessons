n,k = int(input()), int(input())
last = 0
for i in range(1, n+1):
    last = (last + k) % i
print(last + 1)

# В кругу стоят n человек, пронумерованных числами от 1 до n.
# Начинается расчет, при котором каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
# Напишите программу, определяющую номер человека, который останется в кругу последним.
