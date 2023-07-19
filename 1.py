def to_bin(inp):
  inp = int(inp)
  result = []
  while inp != 0:
    result.append(str(inp % 2))
    inp = int(inp / 2)
  return ''.join(result[::-1])

def to_dec(inp):
  inp = inp[::-1]
  result = 0
  for index, value in enumerate(inp):
    result += int(value) * 2**index
  return result  
    
print('Что хотите сделать?')
print('\tПеревести из двоичной в десятичную - 1')
print('\tПеревести из десятичной в двоичную - 2')
print('Введите номер действия: ', end='')

if input() == '1':
  print('(2->10) Введите число для перевода: ', end='')
  inp = input()
  print('Результат перевода: ', to_dec(inp))
if input() == '2':
  print('(10->2) Введите число для перевода: ', end='')
  inp = input()
  print('Результат перевода: ', to_bin(inp))