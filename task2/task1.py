# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input("Введите число: ")
sum = 0
for digit in num:
    if digit.isdigit():
        sum += int(digit)
print("Сумма цифр равна:", sum)
