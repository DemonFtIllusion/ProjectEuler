# Problem 3

# We need to find the largest prime factor of the number
# n = 600851475143
# Therefore a primality test is needed as well.
# Let's be witty, a prime factor of a number n does not go beyond
# the square root of n. So all prime factors of a given number n are
# less than its square root.
# We're going to use that to our advantage.
# Since we now know the prime's factors threshold, we can start from
# there down to a the number we're seeking. There's no need for us
# to test all prime factors starting from 2.

# Let's try and make an isPrime function. I'll try my best
# to optimize its perfomance.

from math import sqrt
from time import perf_counter
Start = perf_counter()

def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False # Every even number except 2 is not prime
    divis = 3
    # We'll start from 3 to the threshold by a step of 2, to avoid even numbers
    # divis < sqrt(n) ::: divis² < n
    # This way we avoid using the sqrt function and the rounding process.
    while divis * divis < n:
        if n % divis == 0:
            return False
        divis += 2
    return True

n = 600851475143
threshold = int(sqrt(n))

# We'll start counting down from threshold, but it's more efficient to avoid even numbers
# like we did in isPrime. If the calculated threshold is even, we add 1 then do our
# tests while decrementing the threshold by a step of 2, otherwise we leave it as it is.

if threshold % 2 == 0: threshold += 1

while n % threshold != 0 and not isPrime(threshold):
    threshold -= 2

End = perf_counter()

print("Result is equal to: ", threshold)
print("Time consumed: ", End-Start, "seconds.")
