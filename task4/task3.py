# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности

from random import randint
n = int(input("Введите количество чисел: "))
res = [round(randint(0, 10), 3) for i in range(n)]
print(res)

found = set()
found_again = set()

for i in range(len(res)):
    if i in found_again:
        continue
    if i in found:
        found.remove(i)
        found_again.add(i)
    else:
        found.add(i)

print(list(found))
