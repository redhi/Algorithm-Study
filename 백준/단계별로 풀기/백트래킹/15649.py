"""
백준 N과 M(1)
"""

import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]
arr2 = list(permutations(arr, M))

for i in range(len(arr2)):
    print(" ".join(map(str, list(arr2[i]))))
