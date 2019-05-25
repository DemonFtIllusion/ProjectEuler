# Problem 20

from time import perf_counter
from math import log2

Start = perf_counter()

Memo = {0: 1}

def Factorial(n):
    if n in Memo: return Memo[n]
    Memo[n] = Factorial(n-1) * n
    return Memo[n]

N = sum([int(c) for c in str(Factorial(100))])

End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
