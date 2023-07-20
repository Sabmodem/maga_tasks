
M = [0,1]

def fib(n):
    if n in range(len(M)):
        return M[n]
    M.append(fib(n - 1) + fib(n - 2))
    return M[-1]
  
for i in range(15):
  print(fib(i))