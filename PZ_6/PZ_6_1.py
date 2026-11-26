# Дан список A размера N. Вывести его элементы в следующем порядке:
# A1, A2, AN, AN-1, A3, A4, AN-2, AN-3, ...
import random

# ввод размера списка с проверкой
while True:
    try:
        n = int(input('Введите размер списка N: '))
        if n > 0:
            break
        print('N должно быть больше 0!')
    except ValueError:
        print('Ошибка, введите целое число!')

# заполнение списка случайными числами
a = []
i = 0
while i < n:
    a.append(random.randint(1, 100))
    i += 1
print('Исходный список:', a)

# формирование результата: два элемента с начала, два с конца
result = []
left = 0
right = n - 1
while left <= right:
    # два элемента с начала: A1, A2, A3, A4, ...
    for _ in range(2):
        if left <= right:
            result.append(a[left])
            left += 1
    # два элемента с конца: AN, AN-1, AN-2, AN-3, ...
    for _ in range(2):
        if left <= right:
            result.append(a[right])
            right -= 1

print('Результирующий список:', result)