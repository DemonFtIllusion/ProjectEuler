# Problem 22

from time import perf_counter
from math import log2

Start = perf_counter()

def score(i, name):
    return i * sum([ord(c) - ord("A") + 1 for c in name])

with open("names.txt", "r") as fin:
    names = sorted([name.replace("\"", "") for name in fin.readline().split(",")])
    N = sum([score(i + 1, name) for i, name in enumerate(names)])

End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
