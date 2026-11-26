# Дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.

while True:
    try:
        n = int(input("Введите размер списка N: "))
        if n < 2:
            raise ValueError
        a = list(map(int, input("Введите элементы через пробел: ").split()))
        if len(a) != n:
            raise ValueError

        # ищем номера (с 1) одинаковых элементов
        found = []
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    found.append((i + 1, j + 1))

        # должна быть ровно одна пара одинаковых элементов
        if len(found) != 1:
            raise ValueError

        print(found[0][0], found[0][1])  # номера по возрастанию
        break
    except ValueError:
        print("Ошибка: нужен список из N целых чисел с ровно двумя одинаковыми элементами.")