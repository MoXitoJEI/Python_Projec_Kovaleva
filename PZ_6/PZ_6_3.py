# Дан список A размера N и целое число K (1 < K < 4, K < N).
# Осуществить циклический сдвиг элементов списка вправо на K позиций
# (при этом A1 перейдет в AK+1, A2 — в AK+2, ..., AN — в AK).
# Допускается использовать вспомогательный список из 4 элементов.

while True:
    try:
        n = int(input("Введите размер списка N: "))
        if n <= 2:
            raise ValueError
        a = list(map(int, input("Введите элементы через пробел: ").split()))
        if len(a) != n:
            raise ValueError
        k = int(input("Введите K (1 < K < 4, K < N): "))
        if not (1 < k < 4 and k < n):
            raise ValueError
        break
    except ValueError:
        print("Ошибка ввода, попробуйте снова.")

# вспомогательный список (не более 4 элементов): последние K элементов
tmp = []
i = n - k
while i < n:
    tmp.append(a[i])
    i += 1

# сдвигаем остальные элементы вправо на K позиций
i = n - 1
while i >= k:
    a[i] = a[i - k]
    i -= 1

# возвращаем сохранённые элементы в начало
i = 0
while i < k:
    a[i] = tmp[i]
    i += 1

print(*a)