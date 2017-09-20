# Problem 2

# F(n) = F(n-1) + F(n-2)
# The first terms are:
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
# The terms we're interested in are:
# 2 8 34 144 610
# Let's see if 34 have a relation between the previous
# two terms that came before it.
# 34 = a * 8 + b * 2 + c
# I noticed that for c = 0, a = 4 and b = 1
# Now let's test it for 144:
# 144 = 4 * 34 + 8 == correct.
# We can prove this by induction OR we can simply implement this in our program
# to see if it results to the correct answer
# We can conclude that the recursive relation goes as follows:
# F(n) = 4 * F(n-1) + F(n-2)
# with the initial values set as:
# F(0) = 2, F(1) = 8


# Dynamic Programmaing FTW!

from time import perf_counter
Start = perf_counter()

Memo = {}

def Fibo(n):
    if n in Memo: return Memo[n]
    if n == 0: return 2
    if n == 1: return 8
    Memo[n] = 4 * Fibo(n-1) + Fibo(n-2)
    return Memo[n]

Term = Fibo(0)
i = 1
while m < 4e6:
    Term += Fibo(i)
    i += 1

End = perf_counter()

print("Result is equal to: ", Term)
print(End-Start, "s")
