# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input("Введите число: "))
fib = [0, 1]
for i in range(n-2):
    to_the_end = fib[-1] + fib[-2]
    to_the_start = (-1)**(i+1)*to_the_end
    fib.append(to_the_end)
    fib.insert(0, to_the_start)
print(*fib)
