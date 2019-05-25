# Problem 21

from time import perf_counter
from math import log2

Start = perf_counter()

def d(n):
    return sum([i for i in range(1, (n // 2) + 1) if n % i == 0])

N = sum([i for i in range(1, 10001) if i == d(d(i)) and i != d(i)])

End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
