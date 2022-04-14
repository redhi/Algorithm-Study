import sys

input = sys.stdin.readline
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]
for i in range(10):
    dp[0][i] = 1
# print(dp)
for i in range(1, n + 1):
    for j in range(len(dp[i])):
        for k in range(j + 1):
            # print(k)
            dp[i][j] += dp[i - 1][k]
# print(dp)
print(dp[n][9] % 10007)
