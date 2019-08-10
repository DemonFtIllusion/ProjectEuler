# Problem 22

from time import perf_counter
from math import log2
import datetime

Start = perf_counter()

N = 0
for i in range(1901, 2001): # between 1901 and 2000
    for j in range(1, 13): # between jan. and dec.
        if datetime.date(i, j, 1).weekday() == 6:
            N += 1

End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
