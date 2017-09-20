# Problem 9

from time import perf_counter

Start = perf_counter()

Found = False
V = 0

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            Found = True
            V = a * b * c
    if Found:
        break
        

End = perf_counter()

print("Result is equal to: ", V)
print("Time consumed: ", End-Start, "seconds.")
