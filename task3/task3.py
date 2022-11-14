# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

from random import randint
n = int(input("Введите количество чисел: "))
res = [round(randint(0, 50)/7, 3) for i in range(n)]
print(res)
mini = res[0]-int(res[0])
maxi = res[0]-int(res[0])
for num in res:
    if num-int(num) > maxi:
        maxi = num-int(num)
    elif num-int(num) < mini:
        mini = num-int(num)
print(round((maxi-mini), 3))
