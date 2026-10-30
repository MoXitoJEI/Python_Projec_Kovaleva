#даны 3 целых числа, одно из которых отлично от двух других, равных между собой.
# Определить порядковый номер числа отличного от них.
while True:
    try:
        A = int(input("Введите A: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")

while True:
    try:
        B = int(input("Введите B:"))
        break
    except ValueError:
        print("Ошибка! Введите целое число")

while True:
    try:
        C = int(input("Введите C: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число")

if A == B:
    result = 3
else:
    if A == C:
        result = 2
    else:
        result = 1

print(result)