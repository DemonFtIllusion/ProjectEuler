# Problem 6

from time import perf_counter

# Sum of Squares from 1 to n = (n^3 / 3) + (n^2 / 2) + (n / 6)
# Square of Sum from 1 to n = (n * (n + 1) / 2)^2
# = (n^2 / 4) * (n^2 + 2*n + 1) = (n^4 / 4) + (n^3 / 2) + (n^2 / 4)

# The difference between Square of Sum and Sum of Squares:
# S(n) = (1/12) * (3*n^4 + 2*n^3 - 3*n^2 - 2*n)

Start = perf_counter()

Diff = lambda n: (1/12) * (3*n**4 + 2*n**3 - 3*n**2 - 2*n)

V = Diff(100)


End = perf_counter()

print("Result is equal to: ", V)
print("Time consumed: ", End-Start, "seconds.")
