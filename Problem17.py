# Problem 17

from time import perf_counter

Start = perf_counter()

special = {11: len("eleven"), 12: len("twelve"), 13: len("thirteen"), 14: len("fourteen"), 15: len("fifteen"), 16: len("sixteen"), 17: len("seventeen"), 18: len("eighteen"), 19: len("nineteen")}

number = {1: len("one"), 2: len("two"), 3: len("three"), 4: len("four"), 5: len("five"), 6: len("six"), 7: len("seven"), 8: len("eight"), 9: len("nine"), 10: len("ten"), 20: len("twenty"), 30: len("thirty"), 40: len("forty"), 50: len("fifty"), 60: len("sixty"), 70: len("seventy"), 80: len("eighty"), 90: len("ninety")}

def countNumber(n):
    if n in number:
        return number[n]
    if n < 100:
        if n in special:
            return special[n]
        else:
            return countNumber(n % 10) + countNumber(n - (n % 10))
    elif 100 <= n < 1000:
        return countNumber(n // 100) + len("hundred") + ((len("and") + countNumber(n % 100)) if (n % 100 != 0) else 0)
    else:
        return len("onethousand")
        
N = 0
for i in range(1, 1001):
    N += countNumber(i)


End = perf_counter()

print("Result is equal to: ", N)
print("Time consumed: ", End-Start, "seconds.")
