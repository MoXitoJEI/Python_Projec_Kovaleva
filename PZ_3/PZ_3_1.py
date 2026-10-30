#Даны три целых числа: (A), (B), (C).
# Проверить истинность высказывания: «Ровно два из чисел (A), (B), (C) являются положительными».
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
        print("Ошибка! Введите целое число.")

while True:
    try:
        C = int(input("Введите C:"))
        break
    except ValueError:
        print("Ошибка! Введите целое число")

count = 0

if A > 0:
    count += 1
if B > 0:
    count += 1
if C > 0:
    count += 1

print(count == 2)

