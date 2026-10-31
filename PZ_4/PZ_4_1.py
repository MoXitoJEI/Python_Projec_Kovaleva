# Дано вещественное число A и целое число N (N > 0).
# Используя один цикл, найти значение выражения:
# 1 - A + A^2 - A^3 + ... + (-1)^N * A^N.
# Условный оператор не использовать.

while True:
    try:
        A = float(input("Введите число A: "))
        N = int(input("Введите число N: "))
        assert N >= 0
        break
    except ValueError:
        print("Ошибка! Введите корректные числа.")
    except AssertionError:
        print("Ошибка! N должно быть неотрицательным.")

S = 0
x = 1
i = 0

while i <= N:
    S += x
    x *= -A
    i += 1

print("Результат:", S)
