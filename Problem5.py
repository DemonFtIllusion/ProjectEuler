# Problem 5

from time import perf_counter

from math import gcd
from functools import reduce

Start = perf_counter()

# We need to find the Least Common Multiple of Numbers in [1..20].
# To compute the LCM(a,b,c), it is equivalent to computing
# LCM(a, LCM(b,c)). We can use reduce for this!!
# Actually, we don't even need the LCM for the range [1..20],
# we can calculate it for [10, 20] and still have the same result.

def LCM(a,b):
    return a*b // gcd(a,b)

value = reduce(LCM, range(10, 21))

End = perf_counter()

print("Result is equal to: ", value)
print("Time consumed: ", End-Start, "seconds.")
