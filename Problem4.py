# Problem 4

from time import perf_counter
Start = perf_counter()

from math import modf

Found = False
N = 997 # Because 999 * 999 = 998001, therefore we start from 997799

while not Found and N >= 100:
    
    Divis = 101 # We start dividing by 100
    Palindrom = int(str(N) + str(N)[::-1]) # Make the Palindrom out of N.
    
    while Divis < 1000:
        Divis += 1
        
        # Get the float value and the integer value of the division.
        (floatV, intV) =  modf(Palindrom / Divis)
        
        if floatV == 0 and intV in range(100, 1000):
            Found = True
            break
    
    N -= 1

# This is the most optimal solution I could think of
# given my current level of Math and Python experience.

        
End = perf_counter()

print("Result is equal to: ", max(res))
print("Time consumed: ", End-Start, "seconds.")
