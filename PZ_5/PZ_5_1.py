# Найти сумму чисел рядя 1,2,3,4,... от числа m. Суммирование оформляется
# функцией с параметрами. Значения m и n программа должна запрашивать
def range_sum (n , m):
    total = 0
    for a in range(n , m + 1):
        total += a
    return total

def check(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print ("Введите другое ЧИСЛОВОЕ значение")


while True:
    n = check("Введите значение n ")
    m = check("Введите значение m ")
    break

print (f"Сумма чисел на промежутке от {n} до {m} равен {range_sum (n , m)}")