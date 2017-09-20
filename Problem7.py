# Problem 7

from time import perf_counter

Start = perf_counter()

def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    divis = 3
    while divis * divis <= n:
        if n % divis == 0:
            return False
        divis += 1
    return True

# We're doing the Brute Force way.

Counter = 2
N = 3
while Counter < 10001:
    N += 2
    if isPrime(N):
        Counter += 1


End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
