# Problem 1

from time import perf_counter
Start = perf_counter()
# We can try and make simple one-liner bruteforce solutions with Python.

# Summation = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
# => Time consumed: 0.00037466650014822216 seconds

# Summation = sum(x for x in range(3, 1000, 3)) + sum(x for x in range(5, 1000, 5))
# => Time consumed: 6.933330251853222e-05 seconds

# OR, we can try figuring out a more sofisticated solution for this, using Math!

# Sum of all multiples of 3 below 1000:
# 3 + 6 + 9 + ... + 999 = 3 * (1 + 2 + 3 + ... + 333) = S1

# Sum of all multiples of 5 below 1000:
# 5 + 10 + 15 + ... + 995 = 5 * (1 + 2 + 3 + ... + 199) = S2

# We sum the two sums together and substract the common multiples like 15, 30, ...
# which is the following sum: 15 + 30 + 45 + ... + 990 = 15 * (1 + 2 + 3 + ... + 66) = S3

# There's a well known formula that calculates the sum of integers from 1 to n
# which is: (n * (n + 1)) // 2

Summation = (3 * 333 * 167) + (5 * 199 * 100) - (15 * 33 * 67)
End = perf_counter()

print(End-Start, "s")
print(Summation)
# Time consumed for Summation = 4.4444424691366805e-07 seconds.
