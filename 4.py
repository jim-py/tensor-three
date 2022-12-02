import math
import cmath
 
print("Введите коэффициенты для уравнения в строчку через пробел: ")
a, b, c = map(float, input("a, b, c = ").split())
 
d = b ** 2 - 4 * a * c
print(f'Дискриминант - {round(d, 2)}')
 
if d > 0:
    print(f'Первый корень - {round((-b + math.sqrt(d)) / (2 * a), 2)} \nВторой корень - {round((-b - math.sqrt(d)) / (2 * a), 2)}')
elif d == 0:
    print(f'Корень - {round(-b / (2 * a), 2)}')
else:
    print(f'Первый корень - {complex(-b, round(math.sqrt(abs(d)), 2))} / {(2 * a)} \nВторой корень - {complex(-b, -round(math.sqrt(abs(d)), 2))} / {(2 * a)}')
