# 가장 큰 증가 부분 수열

import sys
from copy import deepcopy

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = deepcopy(arr)

for i in range(N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
