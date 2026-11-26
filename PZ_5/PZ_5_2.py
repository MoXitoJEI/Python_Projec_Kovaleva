#Описать функцию Power1(A, B) вещественного типа,
# находящую величину AB по формуле AB = exp(B * ln(A)) (параметры A и B — вещественные).
# В случае нулевого или отрицательного параметра A функция возвращает 0.
# С помощью этой функции найти степени AP, BP, CP, если даны числа P, A, B, C.


import math


def power1(a, b):
    if a <= 0:
        return 0.0
    return math.exp(b * math.log(a))


def input_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Ошибка: нужно ввести число. Попробуйте снова.")


p = input_float("Введите P: ")
a = input_float("Введите A: ")
b = input_float("Введите B: ")
c = input_float("Введите C: ")

print(f"A^P = {power1(a, p)}")
print(f"B^P = {power1(b, p)}")
print(f"C^P = {power1(c, p)}")