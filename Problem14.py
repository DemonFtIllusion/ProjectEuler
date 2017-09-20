# Problem 14

from time import perf_counter
from math import log2

Start = perf_counter()

def CollatzLength(n):
    Counter = 1
    while n != 1:
        Counter += 1
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    return Counter

i = 1000000
Longest = 0
while i > 1:
    C = CollatzLength(i)
    if C > Longest:
        N = i
        Longest = C
    i -= 1

End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
