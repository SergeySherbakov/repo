# Вычислить число c заданной точностью d

import math
d = input('Введите число d в формате 0.01 от 10 в степени -1 до 10 в степени -10: ')
d = d[2:len(d)]
print(round(math.pi, len(d)))
