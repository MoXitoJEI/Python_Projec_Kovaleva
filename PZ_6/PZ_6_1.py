# Дан список A размера N. Вывести его элементы в следующем порядке:
# A1, A2, AN, AN-1, A3, A4, AN-2, AN-3, ...

while True:
    try:
        n = int(input("Введите размер списка N: "))
        if n <= 0:
            raise ValueError
        a = list(map(int, input("Введите элементы через пробел: ").split()))
        if len(a) != n:
            raise ValueError
        break
    except ValueError:
        print("Ошибка ввода, попробуйте снова.")

result = []
left, right = 0, n - 1
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

print(*result)