# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input("Введите число: "))
bin_number = []
while number >= 2:
    bin_number.append(str(number % 2))
    number //= 2
bin_number.append(number)
bin_number = [str(i) for i in bin_number]
print(' '.join(bin_number[::-1]))
