from math import pi
from random import uniform

R1 = 10
R2 = R1 / 2

# расчет площади фигуры аналитически
c = 2 * R1 ** 2
a_with_b = (pi * R1 ** 2) / 4
b = (pi * R2 ** 2) / 4
a = a_with_b - b
a_with_c = a + c

# расчет площади фигуры методом Монте-Карло
while True:
    N = int(input('Введите количество точек N: '))
    M = 0

    for i in range(N + 1):
        x = uniform(-R1, R1)
        y = uniform(-R1, R1)

        if (abs(x) <= R1 and abs(y) <= R1 and (x <= 0 and y <= 0 or x >= 0 and y >= 0)) or ((x ** 2 + y ** 2) <= R1 ** 2 and (x ** 2 + y ** 2) >= R2 ** 2 and -R1 < x <= 0 and R1 > y >= 0):
            M += 1

    L = (2 * R1) ** 2
    s_monte_carlo = L * M / N

    print('\n\nРезультат:\n')

    # Вывод ответа
    print('Метод Монте-Карло       ', f'{s_monte_carlo:<.6g} ед. кв.')
    print('Точное значение         ', f'{a_with_c:<.6g} ед. кв.\n')
    print('________________________________________\n')