# Задача: предложить улучшения кода для уже решённых задач: С помощью использования **лямбд, filter, map, zip,
# enumerate, list comprehension

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
# нечётной позиции.

# Было:
n = int(input("Введите количество чисел: "))
res = random.sample(range(1, 50), n)
print(str(res))
sum = 0
for i in range(len(res)):
    if i % 2 == 1:
        sum += res[i]
print(f"Сумма элементов, стоящих на нечетной позиции: {sum}")

# Стало:
res = list(map(int, input().split()))
print(list(enumerate(res)))
sum = 0
for i in range(len(res)):
    if i % 2 == 1:
        sum += res[i]
print(f"Сумма элементов, стоящих на нечетной позиции: {sum}")
