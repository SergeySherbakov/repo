# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

from math import ceil
import random
n = int(input("Введите количество чисел: "))
res = random.sample(range(1, 50), n)
print(str(res))
for i in range(ceil(len(res)/2)):
    print(res[i] * res[-1-i])
