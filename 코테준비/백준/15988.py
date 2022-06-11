# 1,2,3 더하기 3
import sys

input = sys.stdin.readline
d = [0 for _ in range(1000001)]
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, len(d)):
    d[i] = d[i - 1] % 1000000009 + d[i - 2] % 1000000009 + d[i - 3] % 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n] % 1000000009)
