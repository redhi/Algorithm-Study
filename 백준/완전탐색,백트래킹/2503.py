"""
백준 숫자야구
"""

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
baseball = []
for _ in range(N):
    num, s, b = map(int, input().split())
    baseball.append([s, b, list(map(int, list(str(num))))])

arr = [i for i in range(1, 10)]

num = list(permutations(arr, 3))

total = 0
for j in range(len(num)):
    count = 0
    for i in range(N):
        t_s = 0
        t_b = 0
        s = baseball[i][0]
        b = baseball[i][1]
        test = baseball[i][2]
        for k in range(3):
            if test[k] in num[j]:
                if test[k] == num[j][k]:
                    t_s += 1
                else:
                    t_b += 1
        if t_s == s and t_b == b:
            count += 1

    if count == N:
        total += 1

print(total)
