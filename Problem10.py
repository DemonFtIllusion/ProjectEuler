# Problem 10

from time import perf_counter

Start = perf_counter()

def Sieve(n):
    primes = set(range(2, n))
    for i in range(2, n):
        for j in range(i**2, n, i):
            primes.discard(j)
    return sum(primes)

S = Sieve(2000000)

End = perf_counter()

print("Result is equal to: ", S)
print("Time consumed: ", End-Start, "seconds.")
