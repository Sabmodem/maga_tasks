def insertion_sort(a):
  for j in range(len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
      a[i + 1] = a[i]
      i = i - 1
    a[i + 1] = key
  return a  


print('Введите числа для сортировки через запятую (Пример: 1,2,3,4,5): ')
inp = list(map(int, input().split(',')))
print(*insertion_sort(inp))