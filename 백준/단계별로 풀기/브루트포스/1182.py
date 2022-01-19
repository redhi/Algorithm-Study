"""
백준 부분수열의 합
"""
import itertools
import sys

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    comb = itertools.combinations(arr, i)
    for j in comb:
        if sum(j) == S:
            cnt += 1

print(cnt)
