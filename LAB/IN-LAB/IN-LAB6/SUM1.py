def numberOfPaths(m, n):
    if (m == 1 or n == 1):
        return 1
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)
m = 3
n = 3
print(numberOfPaths(m, n))