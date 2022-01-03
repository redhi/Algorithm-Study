"""
백준 점프
DFS
"""
import sys

read = sys.stdin.readline


def dfs(x, y):
    if x == N - 1 and y == N - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        if 0 < x + a[x][y] < N:
            dp[x][y] += dfs(x + a[x][y], y)
        if 0 < y + a[x][y] < N:
            dp[x][y] += dfs(x, y + a[x][y])

    return dp[x][y]


N = int(read())
a = []
cnt = 0

for i in range(N):
    a.append(list(map(int, read().split())))

dp = [[-1] * N for _ in range(N)]

print(dfs(0, 0))
