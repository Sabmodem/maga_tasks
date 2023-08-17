seq = '(fdsf(sdadasf)sad)dsad(sadas)'

def brackets_check(s):
  meetings = 0
  for c in s:
      if c == '(':
          meetings += 1
      elif c == ')':
          meetings -= 1
          if meetings < 0:
              return False
  return meetings == 0

print(brackets_check(seq))