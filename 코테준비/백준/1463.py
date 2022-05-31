import sys

input = sys.stdin.readline
n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    a, b = int(1e9), int(1e9)
    if i % 3 == 0:
        a = dp[i // 3]
    if i % 2 == 0:
        b = dp[i // 2]

    dp[i] = min(a + 1, b + 1, dp[i - 1] + 1)
# print(dp)
print(dp[n])
# 24 1
# 12 2
# 6 3
# 3 4
# 2 5
