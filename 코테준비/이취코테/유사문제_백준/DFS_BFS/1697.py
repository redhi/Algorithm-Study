# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0 for _ in range(100001)]

que = deque()
que.append(n)
while que:
    idx = que.popleft()
    if idx == k:
        print(dp[idx])
        # print(dp)
        break
    for nx in (idx - 1, idx + 1, idx * 2):
        if 0 <= nx < 100001 and not dp[nx]:  # 한번도 방문 안한곳 빼기
            dp[nx] = dp[idx] + 1
            que.append(nx)
