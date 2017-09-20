# Problem 12

from time import perf_counter

Start = perf_counter()

# Total number of divisors of N = Number of divisors below the square root
# of N multiplied by 2.

def Divisors(n):
    Counter = 2 # We already counted 1 and n itself.
    i = 2
    while i*i < n:
        if n % i == 0:
            Counter += 1
        i += 1
    return Counter * 2


Triangular = lambda n : n*(n+1) // 2

i = 1
N = Triangular(i)

while Divisors(N) < 500:
    i += 1
    N = Triangular(i)

End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
