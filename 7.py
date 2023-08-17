seq = 'wabcdcawdawdawda'
substr = 'abc'

def find(substr, seq):
  result = []
  pointer = 0
  for index, sym in enumerate(seq):
    if sym == substr[pointer]:
      result.append(sym)
      pointer += 1
    else:
      result = []
      pointer = 0
    if pointer == len(substr):
      return index - len(substr) + 1
  return -1

print(find(substr, seq))
  