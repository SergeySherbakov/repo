# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число: "))
numbers = range(-n, n+1)
with open('file.txt') as f:
    ids = f.read().split('\n')
prod = 1
for i in ids:
    prod *= numbers[i]
print(prod)
