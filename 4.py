def binSearch(a, key):
    l = -1 # левая граница
    r = len(a) # правая граница
    while l < r - 1: # пока елвая меньше чем правая
        m = int((l + r) / 2) # складываем границы, делим на 2 и отрезаем дробную часть, это будет индекс
        if a[m] < key: # если значение по индексу меньше ключа
            l = m # присваиваем 
        else:
            r = m
    return r if a[r] == key else -1

a = [i for i in range(0, 100, 3)]
print(a)
print(binSearch(a, 45))