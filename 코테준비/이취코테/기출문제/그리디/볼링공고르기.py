import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
d = defaultdict(int)
for a in arr:
    d[a] += 1

dd = []
for key, value in d.items():
    dd.append([key, value])

d = list(d)
dd.sort(key=lambda x: x[0])
count = 0
for i in range(len(dd)):
    summ = 0
    for j in range(i + 1, len(dd)):
        summ += dd[j][1]

    count += dd[i][1] * summ

print(count)
